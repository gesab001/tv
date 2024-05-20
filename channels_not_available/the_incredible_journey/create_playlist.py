import json
import os
import random

def shuffle():
  files = os.listdir()
  #print(files)
  mp4 = []
  for file in files:
    if file.endswith("mp4"):
       mp4.append(file)
  #print(mp4)

  random.shuffle(mp4)
  print(mp4)

  textfile = open("playlist.txt", "w", encoding="utf-8")
  for item in mp4:
   string = "file '"+item+"'"
   textfile.write(string)
   linebreak = "\n"
   textfile.write(linebreak)

  textfile.close()   
