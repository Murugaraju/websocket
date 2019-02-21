# POC code on Websocket
Need redis server running i.e redis-server\
Installation on ubuntu cmd sudo apt-get install redis-server\
check the redis server status by the cmd redis-cli ping, it responds with PONG\
Required python>=3.6 as the current code uses asyncio package\
landing html page url /test/ \
ws url to handshake to the status on model changes i.e. ws://localhost:8000/status/ \
Use https://websoket.org/echo.html to chek the socket connection \
Please use /admin url to login and change records in Model Sample to see the update at websocket client \ 
Use daphne -b 127.0.0.1 -p 8000 websockett.asgi:application or normal django's runserver


