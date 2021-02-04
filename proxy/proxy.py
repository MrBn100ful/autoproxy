import socket, sys, threading, os, time
from mako.template import Template

Socketsrv = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

HOST = "10.0.0.1"

PORT = 2943

SECRET = "supersecret"

try:
    Socketsrv.bind((HOST,PORT))
except socket.error:
    print("Socket error")
    sys.exit()

        
def srv(connexion,adresse):
    while True:
        if connexion:
            while True:
                msgClient = connexion.recv (4096)
                message = msgClient.decode()
                if message == SECRET:
                    msgServeur = "OK"
                    msgServeur = msgServeur.encode()
                    connexion.send(msgServeur)
                    print("Auth ok for",adresse [0], " on port ", adresse [1])
                    msgClient = connexion.recv (4096)
                    message = msgClient.decode()
                    print("The host ip is ",message)
                    mytemplate = Template(filename='template.txt')
                    configf= open("default","w+")
                    configf.write(mytemplate.render(ip=message,date=time.time()))
                    configf.close()
                    os.system('rm /etc/nginx/sites-available/default && cp default /etc/nginx/sites-available/default && systemctl restart nginx')
                    print("new ip set")
                    return
while True:
    Socketsrv.listen(5)
    connexion, adresse = Socketsrv.accept()
    t = threading.Thread(target=srv, args=(connexion,adresse))
    t.start()
