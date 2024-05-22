import subprocess
from create_playlist_json import shuffle
import json

jsonfiles = shuffle()

def getJsonObj(filename):
  fileopen = open(filename, "r", encoding="utf-8")
  jsonobj = json.loads(fileopen.read())
  fileopen.close()
  return jsonobj

def updateJsonObj(video_id):
      command = "yt-dlp "+ video_id + "  --write-info-json --skip-download"
      subprocess.call(command, shell=True)

def streamToFFPLAY(jsonobj):      
      formats = jsonobj["formats"]
      totalformats = len(formats)
      formattype = 13
      formatobj = formats[formattype]
      
      #print(formatobj)
      for x in range(0, totalformats):
        formatobj = formats[x]
        #print(formatobj)
        video_ext = formatobj["video_ext"]
        #print("audio_ext: " + audio_ext)
        #print(video_ext)
        if "mp4" in video_ext:
           acodec = formatobj["acodec"]
           if acodec!="none":
             print(str(x) + ". acodec: " + acodec)                
             formattype = x
      print(formattype)
      #print(mp4s)
      formatobj = formats[formattype]
      url = formatobj["url"]
      command = 'ffplay -i ' +  '"'+url+'"'
      subprocess.call(command, shell=True)
      
for filename in jsonfiles:
  jsonobj = getJsonObj(filename)
  print(filename)
  try:
    video_id = jsonobj["id"]

    #proceed = input("continue: ")
    #if proceed=="y":
    #command = 'ffmpeg -re -i ' +  '"'+url+'"' + ' -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2  -preset fast -b:v 5M -maxrate 6M -bufsize 3M -threads 4 -f flv rtmp://192.168.1.17:1935/show/stream'
    updateJsonObj(video_id)
    jsonobj = getJsonObj(filename)
    #stream(jsonobj)
    streamToFFPLAY(jsonobj)
    #else:
    #  break    
  except Exception as e:
    print("error: " + str(e))
