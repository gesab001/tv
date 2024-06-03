import subprocess
from create_playlist_json import shuffle
import json

port = "1948"

def streamToMacbookProServer():      
      command = 'ffmpeg -f gdigrab -framerate 6 -re -i desktop  -vcodec libx264  -g 30 -acodec aac -strict -2  -preset fast -b:v 5M -maxrate 6M -bufsize 3M -threads 4 -tune zerolatency -f flv rtmp://192.168.1.17:'+port+'/show/stream'
      subprocess.call(command, shell=True)
      

streamToMacbookProServer()