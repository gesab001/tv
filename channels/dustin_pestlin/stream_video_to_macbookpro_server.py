import subprocess
from create_playlist_json import shuffle
import json

jsonfiles = shuffle()
port = "1938"
def getJsonObj(filename):
  fileopen = open(filename, "r", encoding="utf-8")
  jsonobj = json.loads(fileopen.read())
  fileopen.close()
  return jsonobj

def updateJsonObj(video_id):
      command = "yt-dlp "+ video_id + "  --write-info-json --skip-download"
      subprocess.call(command, shell=True)

def stream(jsonobj):      
      formats = jsonobj["formats"]
      totalformats = len(formats)
      formattype = 13
      formatobj = formats[formattype]
      print(formatobj)
      url = formatobj["url"]
      command = 'ffmpeg -re -i ' +  '"'+url+'"' + ' -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2  -preset fast -b:v 5M -maxrate 6M -bufsize 3M -threads 4 -f flv rtmp://a.rtmp.youtube.com/live2/r01k-tjxy-22r2-dudy-5mdf'
      subprocess.call(command, shell=True)

def streamToMacbookProServer(jsonobj):      
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
      command = 'ffmpeg -re -i ' +  '"'+url+'"' + ' -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2  -preset fast -b:v 5M -maxrate 6M -bufsize 3M -threads 4 -f flv rtmp://192.168.1.17:'+port+'/show/stream'
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
    streamToMacbookProServer(jsonobj)
    #else:
    #  break    
  except Exception as e:
    print("error: " + str(e))
#command = 'ffmpeg -re -i "https://rr5---sn-j5aa2a0n-53ae.googlevideo.com/videoplayback?expire=1715467909&ei=JaI_ZpOXJN-k9fwPkMyAoAw&ip=2405%3Ada40%3A1195%3Ac000%3Ad1ba%3A432d%3A5169%3Ace75&id=o-ADNDuAQ0gjS4njsv30hGE7ds_c5-MY-B2OHrf2itxZUB&itag=136&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=in&mm=31%2C26&mn=sn-j5aa2a0n-53ae%2Csn-npoe7nes&ms=au%2Conr&mv=m&mvi=5&pl=41&initcwndbps=2380000&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=1030051589&dur=7045.550&lmt=1712416685506368&mt=1715445894&fvip=2&keepalive=yes&c=IOS&txp=6219224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhANgbD96KkZY1u_Pu7YvCtU6-iKBzD2eo4ReWdFsx5qogAiAFDb4I98OVhEFYaijqV00A5P8J8II_7EggI79svZSr_A%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHWaYeowRAIgYZa8yJYCWHl5S_9-XAIa40TiYHMPE_eRDc2V4mEl5VECIDMNBVIGM3OWgXua4QMPmBXWYSgURTmIFI2XLMP8W-o2" -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://192.168.1.17:1935/show/stream'
command = "ffmpeg -re -f concat -safe 0 -i playlist.txt -r 30 -c:v libx264 -x264-params keyint=60:scenecut=0 -preset fast -b:v 5M -maxrate 6M -bufsize 3M -threads 4 -f flv rtmp://192.168.1.17:1935/show/stream"
#command =  "ffmpeg  -re -f concat -safe 0 -i playlist.txt -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2  -preset fast -b:v 5M -maxrate 6M -bufsize 3M -threads 4 -f flv rtmp://a.rtmp.youtube.com/live2/r01k-tjxy-22r2-dudy-5mdf"
"""
command = 'ffmpeg -re -i "https://rr5---sn-j5aa2a0n-53ae.googlevideo.com/videoplayback?expire=1715467909&ei=JaI_ZpOXJN-k9fwPkMyAoAw&ip=2405%3Ada40%3A1195%3Ac000%3Ad1ba%3A432d%3A5169%3Ace75&id=o-ADNDuAQ0gjS4njsv30hGE7ds_c5-MY-B2OHrf2itxZUB&itag=136&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=in&mm=31%2C26&mn=sn-j5aa2a0n-53ae%2Csn-npoe7nes&ms=au%2Conr&mv=m&mvi=5&pl=41&initcwndbps=2380000&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=1030051589&dur=7045.550&lmt=1712416685506368&mt=1715445894&fvip=2&keepalive=yes&c=IOS&txp=6219224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhANgbD96KkZY1u_Pu7YvCtU6-iKBzD2eo4ReWdFsx5qogAiAFDb4I98OVhEFYaijqV00A5P8J8II_7EggI79svZSr_A%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHWaYeowRAIgYZa8yJYCWHl5S_9-XAIa40TiYHMPE_eRDc2V4mEl5VECIDMNBVIGM3OWgXua4QMPmBXWYSgURTmIFI2XLMP8W-o2" -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2  -preset fast -b:v 5M -maxrate 6M -bufsize 3M -threads 4 -f flv rtmp://a.rtmp.youtube.com/live2/r01k-tjxy-22r2-dudy-5mdf'
"""
#subprocess.call(command, shell=True)
