from Socket import openSocket
from Initialize import joinRoom
from edmcoverlay import Overlay

client = Overlay()

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = readbuffer + s.recv(1024).decode()
    temp = readbuffer.split('\r\n')
    readbuffer = temp.pop()

    for line in temp:
        print(line)
		
		
def say_hello():
    client.send_message(
      msgid="hello-message",
      text="Hello Commander!",
      color="#ff0000",
      size="normal",
      x=200,
      y=200,
      ttl=10)