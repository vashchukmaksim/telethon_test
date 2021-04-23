# README

## Preparation

Create session string to use with `StringSession` and fill `.env` file with corresponding values.

Without `StringSession` I have the following error while run inside docker:

```log
INFO:telethon.network.connection.connection:The server closed the connection
WARNING:telethon.network.mtprotosender:Connection error 1 during auth_key gen: ConnectionError: Not connected
```

## Run without docker

```bash
./run.sh
```

It will create virtual environment, install requirements and run a script. This option works fine on Mac.

## Run with docker (mac)

```bash
docker build -t telethon_test .
docker run telethon_test
```

This option doesn't work:

```log
...
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
INFO:telethon.network.mtprotosender:Connecting to 149.154.167.51:443/TcpFull...
INFO:telethon.network.mtprotosender:Connection to 149.154.167.51:443/TcpFull complete!
INFO:telethon.network.connection.connection:The server closed the connection while sending
INFO:telethon.network.connection.connection:The server closed the connection
INFO:telethon.network.connection.connection:<class 'ConnectionResetError'> during disconnect: [Errno 104] Connection reset by peer
INFO:telethon.network.connection.connection:<class 'ConnectionResetError'> during disconnect: [Errno 104] Connection reset by peer
INFO:telethon.network.mtprotosender:Connection closed while receiving data
INFO:telethon.network.mtprotosender:Closing current connection to begin reconnect...
```
