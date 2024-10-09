import os
from fastapi import FastAPI, HTTPException, Request
from sse_starlette.sse import EventSourceResponse
from fastapi.staticfiles import StaticFiles
from openai import AsyncOpenAI
from fasthtml.common import FastHTML, Html, Head, Title, Body, Div, Button, Textarea, Script, Style, P, Favicon, ft_hx
import bleach

from styles import styles
from script import script
from fasthtml_hf import setup_hf_backup

secret_key = os.getenv('SECRET_KEY')

app = FastHTML(secret_key=secret_key)

app.mount("/static", StaticFiles(directory="static"), name="static")

setup_hf_backup(app)

client = AsyncOpenAI()

conversations = {}

ALLOWED_TAGS = list(bleach.sanitizer.ALLOWED_TAGS) + ["h1", "h2", "h3", "p", "strong", "em", "ul", "ol", "li", "code", "pre", "blockquote"]
ALLOWED_ATTRIBUTES = bleach.sanitizer.ALLOWED_ATTRIBUTES

static_dir = os.path.join(os.path.dirname(__file__), "static")
light_icon = os.path.join(static_dir, "favicon-light.ico")
dark_icon = os.path.join(static_dir, "favicon-dark.ico")

def Svg(*c, viewBox=None, **kwargs):
    return ft_hx('svg', *c, viewBox=viewBox, **kwargs)

def Path(*c, d=None, fill=None, **kwargs):
    return ft_hx('path', *c, d=d, fill=fill, **kwargs)

@app.get("/")
def home():
    """Render homepage with FastGPT UI."""
    home_text = """
## FastGPT - A ChatGPT Implementation Using FastHTML
    """
    
    page = Html(
        Head(
            Title('FastGPT'),
            Favicon(light_icon="/static/favicon-light.ico", dark_icon="/static/favicon-dark.ico"),
            Style(styles),
            Script(src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.2.9/purify.min.js")
        ),
        Body(
            Div(
                Div("FastGPT", _class="logo-text"),
                Div(
                    Button(
                        Svg(
                            Path(
                                d="M441 58.9L453.1 71c9.4 9.4 9.4 24.6 0 33.9L424 134.1 377.9 88 407 58.9c9.4-9.4 24.6-9.4 33.9 0zM209.8 256.2L344 121.9 390.1 168 255.8 302.2c-2.9 2.9-6.5 5-10.4 6.1l-58.5 16.7 16.7-58.5c1.1-3.9 3.2-7.5 6.1-10.4zM373.1 25L175.8 222.2c-8.7 8.7-15 19.4-18.3 31.1l-28.6 100c-2.4 8.4-.1 17.4 6.1 23.6s15.2 8.5 23.6 6.1l100-28.6c11.8-3.4 22.5-9.7 31.1-18.3L487 138.9c28.1-28.1 28.1-73.7 0-101.8L474.9 25C446.8-3.1 401.2-3.1 373.1 25zM88 64C39.4 64 0 103.4 0 152L0 424c0 48.6 39.4 88 88 88l272 0c48.6 0 88-39.4 88-88l0-112c0-13.3-10.7-24-24-24s-24 10.7-24 24l0 112c0 22.1-17.9 40-40 40L88 464c-22.1 0-40-17.9-40-40l0-272c0-22.1 17.9-40 40-40l112 0c13.3 0 24-10.7 24-24s-10.7-24-24-24L88 64z",
                                fill="#b4b4b4"
                            ),
                            viewBox="0 0 512 512",
                            _class="refresh-icon"
                        ),
                        onclick="location.reload()",
                        _class="refresh-button"
                    ),
                    _class='refresh-container'
                ),
                _class="header"
            ),
            Div(
                Div(
                    Div(id="home-text-container", _class="markdown-container", **{"data-home-text": home_text}),
                    _class='title-wrapper'
                ),
                P(id='output'),
                Div(
                    Textarea(
                        id='message',
                        rows=1,
                        cols=50,
                        placeholder="Message FastGPT",
                        oninput="autoResizeTextarea()",
                        onkeypress="checkEnter(event)"
                    ),
                    Button(
                        Svg(
                            Path(
                                d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
                            ),
                            viewBox="0 0 384 512",
                            _class="send-icon"
                        ),
                        onclick="sendMessage()",
                        _class="send-button"
                    ),
                    _class="container"
                ),
                _class="wrapper"
            ),
            Script(script)
        )
    )
    return page

@app.get("/stream")
async def stream_response(request: Request, message: str, session_id: str = None):
    """Stream responses for the given user input."""
    if not message:
        raise HTTPException(status_code=400, detail="Message parameter is required")
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID is required")

    if session_id not in conversations:
        conversations[session_id] = [
            {"role": "system", "content": "You are a helpful assistant. Use Markdown for formatting."}
        ]

    conversations[session_id].append({"role": "user", "content": message})

    async def event_generator():
        try:
            response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversations[session_id],
                stream=True
            )

            assistant_response = ""

            async for chunk in response:
                if await request.is_disconnected():
                    print(f"Client for session {session_id} disconnected")
                    break

                content = chunk.choices[0].delta.content
                if content:
                    assistant_response += content
                    yield {"data": content}

            conversations[session_id].append({"role": "assistant", "content": assistant_response})

        except Exception as e:
            yield {"data": f"Error: {str(e)}"}

        finally:
            print(f"Streaming finished for session {session_id}")

    return EventSourceResponse(event_generator())

@app.get("/reset")
def reset_conversation(session_id: str):
    """Reset the conversation for the specified session ID."""
    if session_id in conversations:
        del conversations[session_id]
    return {"message": "Conversation reset."}