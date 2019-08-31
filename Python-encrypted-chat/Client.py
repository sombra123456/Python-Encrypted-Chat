#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from simplecrypt import encrypt, decrypt
from colorama import Fore, init
init()

print (Fore.RED + "WELCOME TO CRYPT CHAT SERVER\n")
print(Fore.RED + "CLIENT")

x = raw_input("IP: ")
y = input("PORT: ")  

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((x, (y)))

password = raw_input("PASSWORD: ")

while True:
        
        print(Fore.RED + "CLIENT:")
        msg0 = raw_input(">> ")
        ciphertext = encrypt(password, msg0)
        socket_cliente.send(ciphertext)
 
        print(Fore.GREEN + "SERVER:")
        recibido = socket_cliente.recv(1024)
        x = decrypt(password, recibido)
        print("Server>> ", x)
        
 
print ("Adios")
socket_cliente.close()
