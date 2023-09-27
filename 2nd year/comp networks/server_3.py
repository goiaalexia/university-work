import socket
import pickle


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


"""
1. A client sends to the server an array of numbers. Server returns the sum of the numbers
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("172.30.118.87", 7777))
s.listen(5)
cs, addr = s.accept()
b = pickle.loads(cs.recv(4096))
summ = 0
for x in b:
    summ += x
cs.send(str(summ).encode())
cs.close()
"""

"""
2.   A client sends to the server a string. The server returns the count of spaces in the string.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("172.30.118.87", 7777))
s.listen(5)
cs, addr = s.accept()
b = cs.recv(4096).decode()
spaces = 0
for x in b:
    if x == " ":
        spaces += 1
cs.send(str(spaces).encode())
cs.close()
"""

"""
3. A client sends to the server a string. The server returns the reversed string to the client (characters from the end to beginning)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("172.30.118.87", 7777))
s.listen(5)
cs, addr = s.accept()
b = cs.recv(4096).decode()[::-1]
cs.send(b.encode())
cs.close()
"""

"""
4.   The client send to the server two sorted array of chars. The server will merge sort the two arrays and return the result to the client.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.10.127", 7777)) 
s.listen(5)
cs, addr = s.accept()
b1 = pickle.loads(cs.recv(4096))
b2 = pickle.loads(cs.recv(4096))
b1.extend(b2)
merge_sort(b1)
cs.send(pickle.dumps(b1))
cs.close()
"""

"""
# 5.   The client sends to the server an integer. The server returns the list of divisors for the specified number.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.10.127", 7777))
s.listen(5)
cs, addr = s.accept()
b = cs.recv(4096)
b = int.from_bytes(b, "big")
lis = []
i = 2
while (i <= b):
    if b % i == 0:
        lis.append(i)
    i += 1
cs.send(pickle.dumps(lis))
cs.close()
"""

"""
#  6.   The client sends to the server a string and a character. The server
#  returns to the client a list of all positions in the string where specified character is found.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.23.126", 7777))
s.listen(5)
cs, addr = s.accept()
stringy = cs.recv(4096).decode()
c = cs.recv(4096).decode()
lis = []
for i in range(0, len(stringy)):
    if stringy[i] == c:
        lis.append(i)
cs.send(pickle.dumps(lis))
cs.close()
"""

"""
#  7.   The client sends to the server a string and two numbers (s, I, l). The server
#  returns to the client the substring of s starting at index I, of length l.

# suppose the data is right

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.23.126", 7777))
s.listen(5)
cs, addr = s.accept()
c = cs.recv(2)
c = int.from_bytes(c, "big")
e = cs.recv(2)
e = int.from_bytes(e, "big")
stringy = cs.recv(4096).decode()
print(stringy)
stringy = stringy[c:e].encode()
cs.send(stringy)
cs.close()
"""

"""
#  8. The client sends to the server two arrays of integers.
#  The server returns an arrays containing the common numbers found in both arrays.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.23.126", 7777))
s.listen(5)
cs, addr = s.accept()
c1 = pickle.loads(cs.recv(4096))
c2 = pickle.loads(cs.recv(4096))
c3 = set(c1) & set(c2)
print(c3)
cs.send(pickle.dumps(c3))
cs.close()
"""

"""
#  9.   The client sends to the server two arrays of numbers. The server returns
#  to the client a list of numbers that are present in the first arrays but not in the second.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.23.126", 7777))
s.listen(5)
cs, addr = s.accept()
c1 = pickle.loads(cs.recv(4096))
c2 = pickle.loads(cs.recv(4096))
c3 = set.difference(set(c1), set(c2))
print(c3)
cs.send(pickle.dumps(c3))
cs.close()
"""

# 10.The client sends to the server two strings.
# The server sends back the character with the largest number
# of occurrences on the same positions in both strings together with its count.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.23.126", 7777))
s.listen(5)
cs, addr = s.accept()
c1 = cs.recv(4096).decode()
dicty = {}
c2 = cs.recv(4096).decode()
no = 0
l = None
for i in c1:
    if i in dicty.keys():
        dicty[i] += 1
    else:
        dicty[i] = 0
for i in c2:
    if i in dicty.keys():
        dicty[i] += 1
    else:
        dicty[i] = 0
for e in dicty:
    if dicty[e] > no:
        no = dicty[e]
        l = e
cs.send(l.encode())
cs.close()
