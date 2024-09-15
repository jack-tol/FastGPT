styles = """
/* General Styling */
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #212121;
    font-family: 'Inter', sans-serif;
    color: white;
    display: block;
    overflow: auto;
}

p {
    line-height: 1.75;
}

/* Header */
.header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    z-index: 10;
    height: 60px;
}

.logo-text {
    font-size: 40px;
    font-weight: 600;
    color: white;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding-top: 20px;
}

/* Wrapper */
.wrapper {
    margin-top: 60px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    height: calc(100vh - 60px);
    width: 100%;
    padding: 20px 0;
    box-sizing: border-box;
    position: relative;
}

/* Title Section */
.title-wrapper {
    width: 90%;
    max-width: 740px;
    margin-bottom: 10px;
    display: flex;
    justify-content: center;
}

.title {
    color: #b4b4b4;
    margin: 0;
    padding-top: 50px;
    text-align: left;
}

/* Output Section */
#output {
    width: 90%;
    max-width: 740px;
    flex-grow: 1;
    padding: 10px;
    background-color: #212121;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    border-radius: 20px;
    margin: 10px auto;
    box-sizing: border-box;
    max-height: calc(100vh - 180px);
}

/* Container */
.container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #2f2f2f;
    padding: 10px;
    border-radius: 30px;
    width: 90%;
    max-width: 740px;
    min-height: 38px;
    margin: 0 auto;
    box-sizing: border-box;
    position: relative;
    flex-shrink: 0;
}

/* Textarea */
textarea {
    flex: 1;
    background-color: transparent;
    color: #ececec;
    border: none;
    padding: 4px 20px 2px 20px;
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.5;
    resize: none;
    outline: none;
    overflow-y: hidden;
    min-height: 30px;
    max-height: 220px;
    margin: 0;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    flex-shrink: 0;
}

textarea:disabled {
    background-color: #2f2f2f;
    opacity: 0.5;
    cursor: default;
}

textarea::placeholder {
    color: #b4b4b4;
    font-size: 18px;
}

/* Buttons */
.refresh-button, .send-button {
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

/* Refresh Button */
.refresh-button {
    width: 40px;
    height: 40px;
    background-color: transparent;
    border-radius: 50%;
    padding: 0;
}

.refresh-button:hover {
    background-color: #333;
}

.refresh-icon {
    width: 24px;
    height: 24px;
    fill: #b4b4b4;
    transition: fill 0.3s ease;
}

.refresh-button:hover .refresh-icon {
    fill: #fff;
}

/* Send Button */
.send-button {
    background-color: #ffffff;
    color: #212121;
    border-radius: 50%;
    width: 35px;
    height: 35px;
    margin-left: 10px;
    box-sizing: border-box;
    padding: 5px;
    transition: background-color 0.3s ease, fill 0.3s ease;
}

.send-button svg {
    width: 18px;
    height: 18px;
    fill: #000000;
    transition: fill 0.3s ease;
}

.send-button:hover {
    background-color: #ccc;
}

/* Disabled Send Button */
.send-button.disabled {
    background-color: #676767;
    cursor: default;
}

.send-button.disabled svg {
    fill: #2f2f2f;
}

/* Message Styles */
.message.user {
    background-color: #2f2f2f;
    color: white;
    display: inline-block;
    padding: 10px 20px;
    border-radius: 20px;
    max-width: 100%;
    margin: 10px 0;
    align-self: flex-end;
    word-wrap: break-word;
}

.message.ai {
    background-color: transparent;
    color: #f5f5f5;
    display: inline-block;
    padding: 10px 0;
    margin: 10px 0;
    max-width: 100%;
    align-self: flex-start;
    word-wrap: break-word;
}

/* Scrollbars */
#output::-webkit-scrollbar, textarea::-webkit-scrollbar {
    width: 10px;
    background-color: #424242;
}

#output::-webkit-scrollbar-thumb, textarea::-webkit-scrollbar-thumb {
    background-color: #686868;
    border-radius: 5px;
}

#output::-webkit-scrollbar-thumb:hover, textarea::-webkit-scrollbar-thumb:hover {
    background-color: #555;
}

/* Media Queries */
@media (max-width: 768px) {
    #output, .container, .title-wrapper {
        width: 95%;
    }
}
"""