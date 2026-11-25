
# Real-Time Communication with WebSockets

## Description

This project demonstrates how to implement real-time communication between clients and servers using WebSockets in Python.

Unlike traditional HTTP communication, WebSockets maintain a persistent connection that allows clients and servers to exchange messages without opening a new connection for every request.

The project starts with a basic echo server and gradually introduces message validation, multiple client connections, unicast and broadcast communication, ASGI integration, and a browser-based chat interface.

## Learning Objectives

- Understand how WebSocket communication works.
- Use asynchronous programming with `async` and `await`.
- Create WebSocket servers and clients using Python.
- Handle multiple connected clients.
- Validate incoming messages.
- Implement unicast and broadcast communication.
- Build an ASGI application using Starlette.
- Run an application using Uvicorn.
- Connect a browser interface to a WebSocket server.
- Send and receive messages without refreshing the page.

## Technologies Used

- Python 3
- asyncio
- websockets
- Starlette
- Uvicorn
- HTML5
- CSS3
- JavaScript
- WebSocket API

## Project Structure

```text
python_advanced/
└── websockets/
    ├── echo_server.py
    ├── ws_client.py
    ├── validation_server.py
    ├── unicast_server.py
    ├── broadcast_server.py
    ├── asgi_server.py
    ├── index.html
    ├── chat.js
    ├── styles.css
    └── README.md
```

## Tasks

### Task 0: WebSocket Echo Server

File: `echo_server.py`

Creates a basic WebSocket server that listens on port `8765`.

The server accepts multiple client connections, receives messages, and sends each message back to its sender without modification.

Example:

```text
Client: Hello
Server: Hello
```

The connection remains open for continuous communication.

### Task 1: WebSocket Client

File: `ws_client.py`

Creates a WebSocket client that connects to the echo server.

The client:

- Connects to the WebSocket server.
- Sends a text message.
- Receives the server response.
- Prints the response.
- Closes the connection after receiving the message.

Example:

```text
Hello WebSocket
```

### Task 2: Message Validation

File: `validation_server.py`

Adds validation to incoming messages.

The server checks whether a message is empty after removing leading and trailing whitespace.

For valid messages, the server adds the `OK:` prefix.

For empty messages, the server responds with `ERR:EMPTY`.

Examples:

```text
Client: Hello
Server: OK:Hello
```

```text
Client:    
Server: ERR:EMPTY
```

The connection remains open after an invalid message.

### Task 3: Unicast Communication

File: `unicast_server.py`

Implements unicast communication.

The server maintains a set of connected clients and sends each response only to the client that sent the message.

Example:

```text
Client 1: Hello
Server to Client 1: U:Hello
```

Other connected clients do not receive the message.

### Task 4: Broadcast Communication

File: `broadcast_server.py`

Implements broadcast communication.

The server maintains a collection of active connections and sends incoming messages to all connected clients, including the sender.

Example:

```text
Client 1 sends: Hello

Client 1 receives: B:Hello
Client 2 receives: B:Hello
Client 3 receives: B:Hello
```

Disconnected clients are removed from the active connections set.

### Task 5: ASGI Integration

File: `asgi_server.py`

Integrates HTTP and WebSocket communication using Starlette and Uvicorn.

The application provides:

- An HTTP endpoint at `/`.
- A WebSocket endpoint at `/ws`.
- Continuous WebSocket communication.
- Echo functionality for incoming messages.

Uvicorn runs the ASGI application and handles incoming connections.

### Task 6: Browser-Based WebSocket Client

Files:

- `index.html`
- `chat.js`
- `styles.css`

Creates a simple web-based chat interface using HTML, CSS, and JavaScript.

The application allows users to:

- Connect to the WebSocket server.
- Type and send messages.
- Receive messages in real time.
- Display messages without refreshing the page.
- Send multiple messages in one session.

The interface displays sent messages on the right and received messages on the left.

The backend uses echo behavior, so it sends back the same message received from the browser.

## Installation

### 1. Navigate to the Project Directory

```bash
cd holbertonschool-core-engineering/python_advanced/websockets
```

### 2. Install Dependencies

Make sure Python 3 is installed.

Install the required Python libraries:

```bash
python3 -m pip install websockets starlette uvicorn
```

### 3. Verify Installation

```bash
python3 -m uvicorn --version
```

## Running the Project

### Run the Echo Server

```bash
python3 echo_server.py
```

The server listens on:

```text
ws://127.0.0.1:8765/
```

### Run the WebSocket Client

Open another terminal while the echo server is running:

```bash
python3 ws_client.py
```

### Run the Validation Server

```bash
python3 validation_server.py
```

### Run the Unicast Server

```bash
python3 unicast_server.py
```

### Run the Broadcast Server

```bash
python3 broadcast_server.py
```

Note: The standalone servers use port `8765`. Run only one server on this port at a time.

### Run the ASGI Application

Start the Starlette application using Uvicorn:

```bash
python3 -m uvicorn asgi_server:app --host 127.0.0.1 --port 8000 --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The WebSocket endpoint is:

```text
ws://127.0.0.1:8000/ws
```

The `--reload` option automatically restarts the server when Python source files change during development.

## Running in Holberton Sandbox

Holberton Sandbox provides an HTTP preview using port `80`.

To run the browser application in the sandbox, navigate to the project directory and execute:

```bash
python3 -m uvicorn asgi_server:app --host 0.0.0.0 --port 80
```

Then click the **HTTP - Port 80** button in the sandbox interface to open the website.

The browser client uses the current website address to establish its WebSocket connection.

The sandbox gateway must support WebSocket connections for the chat to work.

## Testing

### Test the HTTP Endpoint

With the ASGI server running:

```bash
curl http://127.0.0.1:8000/
```

The application should return the HTML page.

### Test the WebSocket Endpoint

Open a second terminal:

```bash
python3 -m websockets ws://127.0.0.1:8000/ws
```

Send:

```text
Hello
```

Expected response:

```text
Hello
```

### Test the Browser Client

1. Start the ASGI server.
2. Open the website in a browser.
3. Type a message in the input field.
4. Click the Send button.
5. Verify that the message is sent.
6. Verify that the server response appears.
7. Send additional messages without refreshing the page.

### Check Python Code Style

Install pycodestyle if necessary:

```bash
python3 -m pip install pycodestyle
```

Check the Python files:

```bash
pycodestyle *.py
```

## Important Notes

- The standalone WebSocket servers use port `8765`.
- The ASGI application normally uses port `8000`.
- Holberton Sandbox can use port `80` for browser preview.
- Use an IPv4 address such as `127.0.0.1` for local testing.
- The WebSocket connection stays open for continuous communication.
- The browser client communicates with the server without refreshing the page.
- Only one server can listen on the same address and port at a time.
- Press `Ctrl + C` to stop a running server.

## Resources

- [WebSockets Documentation](https://websockets.readthedocs.io/)
- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Starlette Documentation](https://www.starlette.io/)
- [Starlette WebSockets](https://www.starlette.io/websockets/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

## Conclusion

This project demonstrates how to build a real-time communication system using Python and WebSockets.

It covers the development of WebSocket servers and clients, message validation, connection management, unicast and broadcast communication, ASGI integration, and a browser-based chat application.

The final application allows users to send and receive messages through a persistent WebSocket connection without reloading the page.
fdftfhhhhdsuduhg
