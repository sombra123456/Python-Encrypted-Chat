#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from colorama import Fore, init
init()
from simplecrypt import encrypt, decrypt

print(Fore.GREEN + "WELCOME TO CRYPT CHAT SERVER\n")
print(Fore.GREEN + "SERVER")

x = raw_input("IP: ")
y = input("PORT: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((x, (y)))
s.listen(1)

password = raw_input("PASSWORD: ")



while True:
        print ("Waiting for connection...")
        sc, addr = s.accept()
        print ("Client connected from: ", addr)
        
        
        while True:

              recibido = sc.recv(1024)
              x = decrypt(password, recibido)
              
              print(Fore.RED + "CLIENT:")

              if x == "quit":
                      break

              print ("Client: ", x)

              print(Fore.GREEN + "SERVER:")

              msg0 = raw_input(">> ")
              if msg0 == "quit":
                      break
              ciphertext = encrypt(password, msg0)
              sc.send(ciphertext)
 

print ("Adios")
sc.close()
s.close()
