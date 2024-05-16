import re
import os
import json
from create_subtitle_list import makeSublist
import string

def loadBadWords(): 
 currentFolder = os.path.dirname(os.path.realpath("main.py"))
 badwordsfilename = currentFolder + "/badwords2.json"
 json_file = open(badwordsfilename)
 data = json.load(json_file)
 json_file.close()
 return data["badwords"]

def get_sec(time_str):
  """Get Seconds from time."""
  h, m, s = time_str.split(':')
  splitseconds = s.split(",")
  s = splitseconds[0]
  return int(h) * 3600 + int(m) * 60 + int(s) 


def unmaskBadWord(word):
  letters = list(string.ascii_lowercase)
  wordList = list(word)
  for x in range(0, len(wordList)):
    letter = wordList[x]
    letterindex = string.ascii_lowercase.index(letter.lower())
    nextletterIndex = letterindex - 1
    nextletter = letters[nextletterIndex]
    wordList[x] = nextletter

  badword = "".join(wordList)
  return badword
   
def getBadIds(sublist):
  badlanguage = loadBadWords()
  badids = []
  for item in sublist:
    textItem = item["text"]
    start = get_sec(item["time"]["start"])-1
    end = get_sec(item["time"]["end"])+2
    time = [start, end]
    found = []
   # for word in badlanguage:
    #  unmasked = unmaskBadWord(word)
      #p = re.search(r"\b" + re.escape(unmasked) + r"\b", textItem) 
   #   p = re.search(r"\b" + re.escape(unmasked) + r"\b", textItem) 

   #   if p:
     #   found.append(word)
    if item["mute"]:
        badids.append(time)

  #  if len(found)!=0:

   #   badids.append(time)
  return badids  

"""
srt = "../The.Marksman.2021.HDRip.XviD.AC3-EVO.avi-filtered.srt"
sublist = makeSublist(srt)
print(getBadIds(sublist))
"""