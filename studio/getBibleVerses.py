import json
import sys
import os
import requests
import subprocess
def updateTopicList():
	topic_json = "topics3.json"
	if getattr(sys, 'frozen', False):  
	  application_path = os.path.dirname(sys.executable)
	elif __file__:
	  application_path = os.path.dirname(__file__)
	topic_path = os.path.join(application_path, topic_json)
	f = open(topic_path, "r")
	json_data = json.load(f)
	topic = list(json_data.keys())
	raw_data = {"topics": topic} 
	with open("topic.json", "w") as outfile:     
	  json.dump(raw_data, outfile, indent=6)

	
def downloadTopicList():
  command = "curl https://raw.githubusercontent.com/gesab001/bible/master/view1/topics3.json -o topics3.json"
  subprocess.call(command, shell=True)
  
def getTopics(): 
	topic_json = "topic.json"
	if getattr(sys, 'frozen', False):  
	  application_path = os.path.dirname(sys.executable)
	elif __file__:
	  application_path = os.path.dirname(__file__)
	topic_path = os.path.join(application_path, topic_json)
	f = open(topic_path, "r")
	json_data = json.load(f)
	topic = json_data["topics"]
	return topic

    
    
    
    