Daniyal Ibrahim | Telematics Engineer | Python 3.7.5

Internet Programming Python and Javascript

---

Client-/Server-Programming mit WebSockets
============================================


TASK 1
---------

Authentication scenario:

1. the user passes username and password to a client application.
2. a client sends username and password hash to a server 
3. the server checks the data against a list from a file
4. if authentication is correct, it sends a welcome message and waits for further communication.  
   If authentication is incorrect, it sends a rejection message and terminates the connection. 

Create suitable client/server applications with Python using WebSockets.


TASK 2
---------

Scenario of a simple chat application:

1. a client logs on to the server as "active The server records active clients in memory [1] or in a file.
2. a client sends a message to another client (via server). If the client is not active, the message is rejected.
3. a client logs off from the server. The server updates the file of active clients.

Optional: The server logs all chats with timestamp and sender/recipient in a CSV file.

Create suitable client/server applications with Python using WebSockets.

[1] See "Registration" at https://websockets.readthedocs.io/en/stable/intro.html#common-patterns



