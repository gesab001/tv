import os
import io
from bad_word_identifier import loadBadWords, unmaskBadWord, getBadIds
from create_subtitle_list import makeSublist
import re
import platform
import subprocess

def getSubtitleSettings():
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

def generateFilteredSubtitles(videoFilename, videoFolder, srt):   
	print("generateFiltedSubtitles")
	srt = renameFile(srt)
	#srt = renameFile(video)

	srtFolder = os.path.dirname(srt)

    
	f = io.open(srt, encoding='utf-8')
	filtered_srt =  srt + "-filtered.srt"
	filtered_ass = videoFolder +  "/movie-filtered.ass"

	subtitle_string = f.read().strip() 
	f.close()
	json_data = {} 
	badlanguage = loadBadWords()
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
		f = open(filtered_srt, "w", encoding="utf8")
		f.write(subtitle_string)
		#print(subtitle_string)
		f.close()
	except:
		print("error") 
        
	convert_srt_to_ass =  "ffmpeg -i " + filtered_srt + " "  +  filtered_ass
	#print("convert_movie_assfile")
	#print(convert_movie_assfile)
	if platform.system()=="Windows":
	 if os.path.exists(srtFolder + "/assconvert.bat"):
	  os.remove(srtFolder + "/assconvert.bat")
	  if os.path.exists(filtered_ass):
	    os.remove(filtered_ass)
	  outfile = open(srtFolder + "/assconvert.bat", "w")
	  outfile.write(convert_srt_to_ass) 
	  outfile.close()    	 
	  subprocess.call(srtFolder + "/assconvert", shell=True)
	 else:
	  outfile = open(srtFolder + "/assconvert.bat", "w")
	  outfile.write(convert_srt_to_ass) 
	  outfile.close()    	 
	  subprocess.call(srtFolder + "/assconvert", shell=True)
	if platform.system()=="Linux":
	  if os.path.exists(filtered_ass):
	    os.remove(filtered_ass)
	  subprocess.call(convert_srt_to_ass, shell=True)
	sublist = makeSublist(filtered_srt)
	badids = getBadIds(sublist)
	#print(badids)
	subtitle_settings = getSubtitleSettings()

    
	command = "ffplay -vf subtitles=bible-subtitles.ass"+subtitle_settings["bible_style"] + ",subtitles=movie-filtered.ass"+subtitle_settings["movie_style"] + " -i "+ videoFilename

	volumeFilter = " -af \""
	volume = ""
	if len(badids)>0:
	   for start, end in badids:
	    volume += "volume=enable='between(t," + str(start) + "," + str(end) + ")':volume=0, "
	   command = command + volumeFilter + volume
	   command =  command[:-2] + "\""
	else:
   	  command = "ffplay -vf subtitles=bible-subtitles.ass"+subtitle_settings["bible_style"] +  " -i "+ videoFilename    
	return command

      
	
  
""" 
srt = os.path.join("C:\\", "Users", os.getlogin(), "Videos", "The.Forever.Purge.2021.1080p.WEB-DL.DD5.1.H.264-EVO.srt")
video = os.path.join("C:\\", "Users", os.getlogin(), "Videos", "The.Forever.Purge.2021.720p.WEBRip.x264.AAC-[YTS.MX].mp4")
print(generateFilteredSubtitles(video, srt))
"""