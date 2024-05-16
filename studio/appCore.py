from PyQt5.QtWidgets import  QFileDialog
from PyQt5 import QtCore

import subprocess
import re
import json
import string
import datetime
import os
import platform
import sys
from create_subtitle_list import makeSublist
from bad_word_identifier import getBadIds, unmaskBadWord, loadBadWords
from video_filter_generator import generateFilteredSubtitles

def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    splitseconds = s.split(",")
    s = splitseconds[0]
    return int(h) * 3600 + int(m) * 60 + int(s)

def getId(sub):
   id = 1
   return id

def getStart(sub):
  time = '1:23:45'
  result = get_sec(time)
  return result

def getEnd(sub):
  time = '0:00:45'
  result = get_sec(time)
  return result

def getText(sub):
  result = "hello"
  return result

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

	

def showErrorDialog(self, message):
  QErrorMessage.showMessage(self, "eror")
 
def getVideoFile(self):
  filters = "Videos (*.mp4 *.mkv *.mov *.MP4 *.MOV, *.avi)"
  selected_filter = "Videos (*.mp4 *.mkv *.mov *.MP4 *.MOV, *.avi)"
  path = os.path.join("C:\\", "Users", os.getlogin(), "Videos")
  fileObj = QFileDialog.getOpenFileName(self, " Open Video file  ", path, filters, selected_filter)
  return fileObj[0]
  
def getSrtFile(self, videoFolder):
  filters = "SRT (*.srt )"
  selected_filter = "SRT (*.srt)"
  path = os.path.join("C:\\", "Users", os.getlogin(), "Videos")
  fileObj = QFileDialog.getOpenFileName(self, " Open SRT file  ", path, filters, selected_filter)
  return fileObj[0]
  
  
def getCurrentID(totalVerses):
   first_time = datetime.datetime(2018,6,23)
   later_time = datetime.datetime.now()    
   duration = later_time - first_time
   duration_in_s = duration.total_seconds() 
   minutes = divmod(duration_in_s, 60)[0]  
   currentID = minutes
   while currentID>totalVerses:
      currentID = currentID - totalVerses
   return int(currentID)

def getBooks(bible):
  verses = bible 
  books = []
  for verse in verses:
   book = verse["book"]
   if book not in books:
      books.append(book)
  return books
  
def getBibleTopic(topic, bible):
  verses = []  
  if topic=="all":
    verses = bible
  else:
    for item in bible:
        verse = item["word"]
        if topic.lower() in verse.lower():
           verses.append(item)
           #print(verse)		   
  return verses
 
 
def getBookVerses(bookTitle, bible):
    verses = []
    for item in bible:
        verse = item["book"]
        if bookTitle.lower() in verse.lower():
           verses.append(item)
           #print(verse)		   
    return verses
    

def getVerse(id, bible):

	verse = bible[id-1]
	return verse
   
def getMinute(minutes):
   result = '{:02d}:{:02d}:00,000'.format(*divmod(minutes, 60 ))
   return result


def showProgress(self):
    self.progress_dialog = QtWidgets.QProgressDialog("Analysing subtitles...", "Abort Copy", 0, 10, self)
    self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
    self.progress_bar = QtWidgets.QProgressBar(self.progress_dialog)
    self.progress_bar.setTextVisible(False)
    self.progress_dialog.setBar(self.progress_bar)
    self.progress_dialog.setMaximum(10)
    self.progress_dialog.setWindowTitle("Picasso: ToRaw")
    self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
    self.progress_dialog.show() 
    
    
def getWordList(setValue, sublist, badlanguage):
	#showProgress(self)
    
	result = []    
	for i in range(0, len(sublist)-1):
	 #print(sublist[i]+"\n\n")
	 id = i 
	 loop = QtCore.QEventLoop()
	 QtCore.QTimer.singleShot(1, loop.quit)
	 loop.exec_()
	 setValue(i+1)    
	 split = sublist[i].split("\n")
	 
	 time = split[1]
	 timesplit  = time.split(" --> ")
	 #print(timesplit)
	 start = get_sec(timesplit[0])-1
	 end = get_sec(timesplit[1])+2
	 
	 #print(word_list)
	 #print(word)
	 #print(split[2])
	 time = [start, end]
	 text = split[2].lower()
	 if len(split)>3:
	    text+= " " + split[3].lower() 
	 textSplit = text.split(" ")
	 badlanguagelist = []
	 for word in badlanguage:
	  unmasked = unmaskBadWord(word)
	  badlanguagelist.append(unmasked) 
	 for item in textSplit:
	  word = re.sub(r"[^a-zA-Z]","", item)  
	  for bad in badlanguagelist:
	    p = re.search(r"\b" + re.escape(bad) + r"\b", word) 
	    x = re.findall(r'\b'+bad+'\w+', word)    
	    if p or x:
 	      print("pass")
	    else:  
	      if len(word.lower())>2 and word.lower() not in result and word.lower() not in badlanguagelist: 
	        result.append(word.lower())          
	 text = ""
	sortedList = sorted(result)
	return sortedList

	#print("badids: " + str(badids))
	#print("total:" + str(numberofbadlanguage))
 
def getBible(self): 
	bible_json = "bible.json"
	if getattr(sys, 'frozen', False):  
	  application_path = os.path.dirname(sys.executable)
	elif __file__:
	  application_path = os.path.dirname(__file__)
	bible_path = os.path.join(application_path, bible_json)
	f = open(bible_path, "r")
	json_data = json.load(f)
	bible = json_data["bible"]
	return bible

def getTopics(self): 
	topic_json = "topic.json"
	if getattr(sys, 'frozen', False):  
	  application_path = os.path.dirname(sys.executable)
	elif __file__:
	  application_path = os.path.dirname(__file__)
	topic_path = os.path.join(application_path, topic_json)
	f = open(topic_path, "r")
	json_data = json.load(f)
	topic = json_data["topic"]
	return topic    
   
def saveGeneratedBibleSubtitles(totalVerses, bible, videoFolder):
	#print("line 266: " + str(bible))
	length = 240
	id = "1"
	start = "00:00:00,000" 
	to = "-->"
	end = " 00:01:00,000"
	words = "Is that you on the beach?"
	toString = id + "\n" + start + "\n" + to + "\n" + end + "\n" + words + "\n\n"
	currentID =  getCurrentID(totalVerses) 
	subtitles = ""
	for i in range(1, length, 1):
		id = str(i)
		start = getMinute(i-1)
		end = getMinute(i)
		verse = getVerse(currentID, bible)	
		words = verse["word"] + " " + verse["book"] + " " + str(verse["chapter"]) + ":" + str(verse["verse"])
		toString = id + "\n" + start + " " + to + " " + end + "\n" + words + "\n\n"
		#print(toString)
		currentID = currentID + 1
		if currentID>totalVerses:
		  currentID = 1
		subtitles = subtitles + toString
	print("total verses: " + str(totalVerses))	

	outfile = open(videoFolder + "/bible-subtitles.srt", "w")
	outfile.write(subtitles)
	outfile.close()
	bibleassfile = videoFolder + "/bible-subtitles.ass"
	if os.path.exists(bibleassfile):
	  os.remove(bibleassfile)
	else:
	  print("The file does not exist")
	convertoass =  "ffmpeg -i " + videoFolder + "/bible-subtitles.srt " + bibleassfile
	subprocess.call(convertoass, shell=True)
    
def generateBibleSubtitles(self, choice, topic):


	totalVerses = 0
	json_data = getBible(self)

	#print("line 250 json_data: " + str(json_data))
	bible = []


	if choice=="book":
	 books = getBooks(json_data)
	 #print(str(books) + " line 256")

	 for book in books:
	  if topic.lower() == book.lower():
	   bookName = book
	   bible = getBookVerses(bookName, json_data)
	else:  

	 bible = getBibleTopic(topic, json_data)  
	 #print("bible topics") 
	 #print(bible) 

	totalVerses = len(bible)
	return {"totalVerses": totalVerses, "bible": bible}

    


def generateFiltedSubtitles(videoFolder, badlanguage,subtitle_string,movie_subtitle_file, movie_assfile):   
	print("generateFiltedSubtitles")

	for word in badlanguage:
	 unmasked = unmaskBadWord(word)
	 #print(unmasked)
	 if re.search(unmasked, subtitle_string, re.IGNORECASE):
	     r = re.compile(r"\b"+re.escape(unmasked)+ r"\b", re.IGNORECASE)
	     subtitle_string = r.sub(r'***', subtitle_string)
	     r = re.compile(r'\b'+unmasked+'\w+', re.IGNORECASE)
	     subtitle_string = r.sub(r'***', subtitle_string)

	#subprocess.call("bible", shell=True)	
	#print(subtitle_string)
	try:
		f = open(movie_subtitle_file, "w", encoding="utf8")
		f.write(subtitle_string)
		#print(subtitle_string)
		f.close()
	except:
		print("error") 
	convert_movie_assfile =  "ffmpeg -i " + movie_subtitle_file + " "  + videoFolder + "/" + movie_assfile
	print("convert_movie_assfile")
	print(convert_movie_assfile)
	if platform.system()=="Windows":
	 if os.path.exists(videoFolder + "/assconvert.bat"):
	  os.remove(videoFolder + "/assconvert.bat")
	  if os.path.exists(movie_assfile):
	    os.remove(movie_assfile)
	  outfile = open(videoFolder + "/assconvert.bat", "w")
	  outfile.write(convert_movie_assfile) 
	  outfile.close()    	 
	  subprocess.call(videoFolder + "/assconvert", shell=True)
	 else:
	  outfile = open(videoFolder + "/assconvert.bat", "w")
	  outfile.write(convert_movie_assfile) 
	  outfile.close()    	 
	  subprocess.call(videoFolder + "/assconvert", shell=True)
	if platform.system()=="Linux":
	  if os.path.exists(movie_assfile):
	    os.remove(movie_assfile)
	  subprocess.call(convert_movie_assfile, shell=True)	
    
def setSubtitleSettings():
	position_bible = "2" #input("bible verse position(6=top,2=bottom)")
	repeat = "1" #input("repeat (0=forever): ")
	adjust_time = 0 #int(input("adjust time: "))
	position_movie = "6"
	if position_bible=="6":
	  position_movie = "2"
	elif position_bible=="2":
	  position_movie = "6"  
	bible_style = ":force_style='Alignment="+position_bible+"'"
	movie_style = ":force_style='Alignment="+position_movie+"'"
	return {"bible_style": bible_style, "movie_style": movie_style}



def renameFile(old_file_name):
	new_file_name = old_file_name.replace(" ", "_")
	os.rename(old_file_name, new_file_name)
	return new_file_name
 
def playVideo(self, video, srt, choice, topic):
	videoFolder = os.path.dirname(video)
	print("playVideo function")
	print(videoFolder)
    
	bibleSubtitlesObj = generateBibleSubtitles(self, choice, topic)   
	totalVerses = bibleSubtitlesObj["totalVerses"]
	if totalVerses>0:
	  saveGeneratedBibleSubtitles(totalVerses, bibleSubtitlesObj["bible"], videoFolder)
	  command = generateFilteredSubtitles(video, videoFolder, srt)
	  if platform.system()=="Windows":
	    outfile = open(videoFolder + "/play.bat", "w")
	    outfile.write(command)
	    outfile.close()    
	    subprocess.call("cd " + videoFolder + " && play", shell=True)	  
	  if platform.system()=="Linux":
	    subprocess.call(command, shell=True)
	else:
	  print("no bible verses found for selected topic. choose another one")
	  self.showPopUpInfo("Topic", "no bible verses found for '" + topic + "'. choose another one", "select a word from the topic list to generate bible verses where the word is found")      

     
        

def playVideoWithoutSubs(self, video, choice, topic):
	videoFolder = os.path.dirname(video)
	generateBibleSubtitles(self, choice, topic)

	subtitle_settings = setSubtitleSettings()

	command = "ffplay -vf subtitles=bible-subtitles.ass"+subtitle_settings["bible_style"] +  " -i "+ video

	if platform.system()=="Windows":
	  outfile = open(videoFolder + "/play.bat", "w")
	  outfile.write(command)
	  outfile.close()    
	  subprocess.call("cd " + videoFolder + " && play", shell=True)	  
	if platform.system()=="Linux":
	  subprocess.call(command, shell=True)

