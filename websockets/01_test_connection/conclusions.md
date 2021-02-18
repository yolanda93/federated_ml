- **Problem description**: PySyft does not provide appropiate methods to leave the WebSocket Server operate with the data (read or write). 
- **Posible Workaround**: Launch a thread from the main server process and access shared memory to concurrently read server data while listens new incomming messages. 

------
**Take aways**

Although a solution might be implemented for this use case. This use case is not a good architectural design. The one with the responsability to order these operations (read and write) is the client.
The server is not allowed to order operations (it acts like a slave).

The most important take aways from this PoC is that there is a strong segregation of responsabilities in PySyft:
  * **Client** (master): orders operations to be executed
  * **Server** (slave): executes operations
