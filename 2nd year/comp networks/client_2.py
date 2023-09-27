import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "\u001b[31m lol"
s.sendto(str.encode(msg), ("172.30.116.199", 5555))
msg, adr = s.recvfrom(10) # buffer + address
print(msg.decode())


