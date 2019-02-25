# POC code on Websocket

1. Need redis server running i.e redis-server
2. Installation on ubuntu cmd sudo apt-get install redis-server
3. check the redis server status by the cmd redis-cli ping, it responds with PONG
4. Required python>=3.6 as the current code uses asyncio package
5. landing html page url /test/ 
6. ws url to handshake to the status on model changes i.e. ws://localhost:8000/status/ 
7. Use https://websoket.org/echo.html to chek the socket connection 
8. Please use /admin url to login and change records in Model Sample to see the update at websocket client
9. Use daphne -b 127.0.0.1 -p 8000 websockett.asgi:application or normal django's runserver 


