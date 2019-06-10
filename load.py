def plugin_start(plugin_dir):
   """
   Load this plugin into EDMC
   """
   print "I am loaded! My plugin folder is {}".format(plugin_dir.encode("utf-8"))
   return "I am loaded!"
   
      

   def plugin_stop():
    """
    EDMC is closing
    """
    print "Farewell cruel world!"
	
import os
import traceback
import requests
import Tkinter as tk
try:
    import myNotebook as nb
    from config import config
    from EDMCOverlay import edmcoverlay
except ImportError:  ## test mode
    nb = None
    config = dict()
    edmcoverlay = None	


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
