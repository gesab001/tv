from subprocess import Popen, PIPE
import os
import json
import random
import subprocess

channels = os.listdir("../channels")
print(channels)
jsonobjChannels = {"channels": {}}

    

def getJsonObj(filename):
  fileopen = open(filename, "r", encoding="utf-8")
  jsonobj = json.loads(fileopen.read())
  fileopen.close()
  return jsonobj
  
def updateJsonObj(channelfolder, video_id):
      command = "cd ../channels/"+channelfolder + " && yt-dlp "+ video_id + "  --write-info-json --skip-download"
      subprocess.call(command, shell=True)
      
def shuffle(folder):
  files = os.listdir(folder)
  #print(files)
  jsonFiles = []
  for file in files:
    if file.endswith("json"):
       jsonFiles.append(file)
  #print(mp4)

  random.shuffle(jsonFiles)
  return jsonFiles    
  
def getVideoUrl(jsonobj):      
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
      return url


      
      
for channel in channels:  
  jsonfiles = shuffle("../channels/"+channel)
  jsonobjChannels["channels"][channel] = {"channelName": "", "videos": []}  
  filename = jsonfiles[0]
  jsonobjItem = getJsonObj("../channels/"+channel+"/"+filename)
  try:
      video_id = jsonobjItem["id"]
      updateJsonObj(channel, video_id)
      jsonobjItem = getJsonObj("../channels/"+channel+"/"+filename)
      channelName = jsonobjItem["channel"]
      videoTitle = jsonobjItem["title"]
      videoUrl = getVideoUrl(jsonobjItem)
      
      jsonobjChannels["channels"][channel]["channelName"] = channelName
      videoObj = {"title": videoTitle, "url": videoUrl}
      jsonobjChannels["channels"][channel]["videos"].append(videoObj)      
      #else:
      #  break    
  except Exception as e:
      print("error: " + str(e))  
  
with open("channel_choices.json", "w") as outfile:
   json.dump(jsonobjChannels, outfile, indent=4)     
  