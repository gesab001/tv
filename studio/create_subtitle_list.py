import re

def makeSublist(srt):
    print("makeSublist")

    #print(srt)
    f = open(srt, "r",  encoding="utf8")
    #subtitle_string = f.read()
    oldNumber = 0
    text = ""
    item = {}
    sublist = []
    for x in f:
     try:
      newNumber = int(x)
      difference = newNumber - oldNumber
      #print(difference)
      oldNumber = newNumber
      if difference!=1:
        #print("its a text")
        text = x
        item["text"] = text.strip()
        number = item["number"]
        sublist.append(item)  
        item = {}
        text = ""  
      else:
        item["number"] = int(x)
        item["text"] = text.strip()
        if "***" in item["text"]:
          item["mute"] = True
        else:
          item["mute"] = False        
        #print(item)
        sublist.append(item)  
        item = {}
        text = ""  
     except:
       if "-->" in x:
         item["time"] = {}
         timesplit = x.strip().split(" --> ")
         item["time"]["start"] = timesplit[0]
       
         item["time"]["end"] = timesplit[1]
       else:
         text = text + x
         
         
     
    #print(sublist)
    #print(len(sublist))
    f.close()
    del sublist[0]
    return sublist

