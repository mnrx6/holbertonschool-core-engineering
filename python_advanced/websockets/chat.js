
const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const socket = new WebSocket(`${protocol}//${window.location.host}/ws`);

const messages = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");

socket.onopen = function () {
    console.log("Done!");
};

socket.onmessage = function (event) {
    const paragraph = document.createElement("p");
    paragraph.textContent = event.data;
    paragraph.classList.add("received");
    messages.appendChild(paragraph);
};

sendButton.addEventListener("click", function () {
    const text = messageInput.value;

    if (socket.readyState === WebSocket.OPEN && text.trim() !== "") {
        socket.send(text);

        const paragraph = document.createElement("p");
        paragraph.textContent = text;
        paragraph.classList.add("sent");
        messages.appendChild(paragraph);

        messageInput.value = "";
    }
});
