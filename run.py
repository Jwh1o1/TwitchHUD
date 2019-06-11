import string
from Socket import openSocket
from Initialize import joinRoom
from read import getUser, getMessage

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = readbuffer + s.recv(1024).decode()
    temp = readbuffer.split('\r\n')
    readbuffer = temp.pop()

    for line in temp:
        print(line)
f=open('chatlog.txt'), ('a+')
f.write('(line)' + '\r\n')