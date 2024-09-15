script = """
// Generate a new session ID on every page load
let sessionId = Math.random().toString(36).substring(2);

// Handle page load
window.onload = function() {
    autoResizeTextarea();  // Handle the initial state of the textarea
    renderHomeText();      // Render the home text (markdown content)
};

// Function to handle sending a message
async function sendMessage() {
    const messageElem = document.getElementById('message');
    const sendButton = document.querySelector('.send-button');
    const message = messageElem.value.trim();

    // Return early if the message is empty
    if (!message) return;

    const output = document.getElementById('output');

    // Disable textarea and button while processing
    messageElem.disabled = true;
    sendButton.disabled = true;
    sendButton.classList.add('disabled'); // Visual indication

    // Display user's message in the chat
    const userMessage = document.createElement('p');
    userMessage.classList.add('message', 'user');
    userMessage.innerHTML = message.replace(/\\n/g, '<br>'); // Preserve line breaks
    output.appendChild(userMessage);

    // Clear the textarea and reset its height
    messageElem.value = '';
    autoResizeTextarea();

    // Scroll to the bottom of the output
    output.scrollTop = output.scrollHeight;

    // Create a new div for the AI's response
    let aiMessage = document.createElement('p');
    aiMessage.classList.add('message', 'ai');
    output.appendChild(aiMessage);

    // Open a connection to stream the AI's response
    const eventSource = new EventSource(`/stream?message=${encodeURIComponent(message)}&session_id=${encodeURIComponent(sessionId)}`);
    let partialResponse = ''; // Accumulate streaming response

    eventSource.onmessage = function(event) {
        partialResponse += event.data;

        // Convert markdown to HTML and sanitize it
        const sanitizedHtml = DOMPurify.sanitize(marked.parse(partialResponse));
        aiMessage.innerHTML = sanitizedHtml;
        output.scrollTop = output.scrollHeight; // Scroll to the bottom
    };

    // Handle errors during the SSE connection
    eventSource.onerror = function() {
        console.error("Error occurred with SSE");
        resetInputState(messageElem, sendButton); // Re-enable input on error
        eventSource.close(); // Close the connection
    };

    eventSource.onopen = function() {
        console.log("Connection to server opened.");
    };

    // Re-enable textarea and button after the AI finishes responding
    eventSource.onclose = function() {
        console.log("Connection to server closed.");
        resetInputState(messageElem, sendButton); // Re-enable input after response
    };
}

// Function to reset the input state (re-enable textarea and send button)
function resetInputState(messageElem, sendButton) {
    messageElem.disabled = false;
    sendButton.disabled = false;
    sendButton.classList.remove('disabled');
    messageElem.focus();
}

// Auto-resize the textarea as the user types and manage send button state
function autoResizeTextarea() {
    const textarea = document.getElementById('message');
    const sendButton = document.querySelector('.send-button');
    
    textarea.style.height = 'auto'; // Reset height to auto
    const maxHeight = 220;
    let newHeight = textarea.scrollHeight;

    if (newHeight > maxHeight) {
        textarea.style.height = maxHeight + 'px';
        textarea.style.overflowY = 'auto';
    } else {
        textarea.style.height = newHeight + 'px';
        textarea.style.overflowY = 'hidden';
    }

    // Enable/disable the send button based on textarea content
    sendButton.disabled = textarea.value.trim() === '';
    sendButton.classList.toggle('disabled', !textarea.value.trim());
}

// Enable sending message on Enter key press (without shift)
function checkEnter(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
}

// Function to render home page text from Markdown (on page load)
function renderHomeText() {
    const homeTextContainer = document.getElementById('home-text-container');
    const markdownContent = homeTextContainer.getAttribute('data-home-text');

    // Parse markdown and sanitize HTML
    const sanitizedHtml = DOMPurify.sanitize(marked.parse(markdownContent));
    homeTextContainer.innerHTML = sanitizedHtml;
}
"""