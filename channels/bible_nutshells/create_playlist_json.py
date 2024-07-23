import json
import os
import random

def shuffle():
  files = os.listdir()
  #print(files)
  jsonFiles = []
  for file in files:
    if file.endswith("json"):
       jsonFiles.append(file)
  #print(mp4)

  random.shuffle(jsonFiles)
  return jsonFiles
