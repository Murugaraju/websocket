Need redis server running i.e redis-server
Installation on ubuntu cmd sudo apt-get install redis-server
check the redis server status by the cmd redis-cli ping, it responds with PONG
Required python>=3.6 as the current code uses asyncio package
landing html page url /test/
ws url to handshake to the status on model changes is ws://localhost:8000/status/
Use https://websoket.org/echo.html to chek the socket connection 
Please use /admin url to login and change records in Model Sample to see the update at websocket client


