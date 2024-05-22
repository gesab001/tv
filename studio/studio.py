from subprocess import Popen, PIPE
import os

channels = os.listdir("../channels")
print(channels)

channels_to_stream = []
for x in range(0, len(channels)):
  index = str(x)
  folder = channels[x]
  print (index +". " + folder)
while True:
  indexInput = input("select channel: (type 'finish' to continue)")
  if indexInput=="finish":
    break
  else:  
    folder = channels[int(indexInput)]
    channels_to_stream.append(folder)

print(channels_to_stream)
proceed = input("broadcast these channels? ")
if proceed.lower()=="y":  
 for channel in channels_to_stream:
   cmd =  "cd .. && cd channels && cd "+channel+" && py stream_video_to_macbookpro_server.py"
   process1 = Popen(cmd, shell=True)
