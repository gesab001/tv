import subprocess
import re
import json
import string
import datetime
import os
import platform
import sys


def checkCookieFromEdge():
  path = os.path.join("C:\\", "Users", os.getlogin(), "Downloads", "youtube.com_cookies.txt")
  if os.path.exists(path):
    return path
  else:
    return False
  
def checkCookieFromFirefox():
  return true

def checkCookieFromChrome():
  return
  
def getCookie(browser):
  if browser=="edge":
    path = checkCookieFromEdge()
    return path
  if browser=="firefox":
    path = checkCookieFromFirefox()
    return path
def download(youtubeId):
   
    try:
      path = os.path.join("C:\\", "Users", os.getlogin(), "Videos")
      cookiePath = getCookie("edge")
      if cookiePath==False and platform.system()=="Windows":
        print("this video is restricted so it requires that you are signed into your youtube account for age verification.  install 'Get cookies.txt' addon in Microsoft Edge, then login to your youtube account, and click on the 'Get cookies.txt' to download cookies. Ensure the cookies file is in the Downloads folder. The Youtube Downloader will use this cookie file to downloaded age restricted videos.  Try downloading again.")
      else:
        command = "youtube-dl --restrict-filenames --write-auto-sub --sub-lang en --cookies \"" + cookiePath+"\" -f mp4 --convert-subs srt " + youtubeId +" --output " + path +  "\\%(uploader)s%(title)s.%(ext)s"
        print(command)
        subprocess.call(command, shell=True)
    except IndexError as error:
      print(error)