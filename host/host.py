import  socket , sys, threading
from requests import get

IP = get('https://api.ipify.org').text

SOCKET = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

HOST = "10.0.0.1" # the static ip ( your cheap vps )

PORT = "2943" # both need to be the same

SECRET = "supersecret" # to have a bit a security 


try:
    SOCKET.connect ((HOST ,int(PORT)))
except socket.error:
    print("Socket error")
    sys.exit()
while True:
    msgClient = SECRET
    msgClient = msgClient.encode()
    SOCKET.send(msgClient)
    msgServeur = SOCKET.recv (4096)
    message = msgServeur.decode()
    if message == "OK":
        msgClient = IP
        msgClient = msgClient.encode()
        SOCKET.send(msgClient)
        SOCKET.close()
        sys.exit()
