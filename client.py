import socket
import threading
from GenerateNumbers import *
from Encryption import *
from Decryption import *
import sys
from termcolor import colored, cprint


choice=input("Do you want to host (1) or connect (2)?")
username=input("Please enter your name:")

HOST="127.0.0.1"
PORT=3000

publicKey,N,privateKey=GenerateRequiredNumbers()
public_partner=None
partner_name=None
partner_N=None

if choice=="1":
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()
    client , _=server.accept()

    client.send(bytes(str(publicKey),"utf-8"))
    public_partner= client.recv(1024).decode("utf-8")
    client.send(bytes(username,"utf-8"))
    partner_name= client.recv(1024).decode("utf-8")
    client.send(bytes(str(N),"utf-8"))
    partner_N= client.recv(1024).decode("utf-8")

elif choice=="2":
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    public_partner= client.recv(1024).decode("utf-8")
    client.send(bytes(str(publicKey),"utf-8"))
    partner_name= client.recv(1024).decode("utf-8")
    client.send(bytes(username,"utf-8"))
    partner_N= client.recv(1024).decode("utf-8")
    client.send(bytes(str(N),"utf-8"))
else:
    exit()

def sending_message(user):
    while True:
        message=input("")
        sentMsg=encrypt(str(message),int(public_partner),int(partner_N))
        user.send(bytes(sentMsg,"utf-8"))


def receiving_message(user): 
    while True:
        msg=user.recv(1024).decode()
        finalText=decrypt(str(msg),privateKey,N)
        text = colored(f"{partner_name} : "+finalText, 'blue')
        print(text)

threading.Thread(target=sending_message,args=(client,)).start()
threading.Thread(target=receiving_message,args=(client,)).start()      