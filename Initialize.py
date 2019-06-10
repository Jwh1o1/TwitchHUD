from Socket import sendMessage
def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode()
        temp = readbuffer.split('\r\n')
        readbuffer = temp.pop()

        for line in temp:
            print (line)
            Loading = loadingComplete(line)
    sendMessage(s, "Successfully joined chat!")

def loadingComplete(line):
    if("End of /NAMES list"):
        return False
    else:
        return True