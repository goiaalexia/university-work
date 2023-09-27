import time
import socket
import random
from threading import Thread


def handle_client(cs, i, wordy):
    print("Handling  client [" + str(i) + "]")
    print(wordy)
    wordy_l = list(wordy)
    current_guess = list()
    word_len = len(wordy)
    tries = 3
    for c in wordy:
        current_guess.append("_")
    while True:
        ok = 0
        rcv = cs.recv(1)
        cr = rcv.decode()
        print(word_len)
        cc = 0
        for cc in range(int(word_len)):
            print(wordy_l)
            print(cr)
            print(cc)
            if wordy_l[cc] == cr:
                current_guess[cc] = wordy_l[cc]
                ok = 1
                print(current_guess)
        if ok == 0:
            tries -= 1
            break
        if tries == 0:
            cs.send(f"You lost, word was: {''.join(wordy_l)}".encode())
            cs.close()
            break
        elif current_guess == wordy_l:
            cs.send(f"You won, word was: {''.join(wordy_l)}".encode())
            cs.close()
            break
        else:
            cs.send(''.join(current_guess).encode())


words = ["mouse", "laptop", "book"]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 7777))
s.listen(5)
i = 0
while True:
    i = i + 1
    cs, address = s.accept()
    t = Thread(target=handle_client, args=(cs, i, random.choice(words)))
    t.start()
