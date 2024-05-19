from subprocess import Popen, PIPE
import os

channels = os.listdir("../channels")
print(channels)
cmd1 = "cd .. && cd channels && cd ernie_knoll && py stream_video_to_macbookpro_server.py"
cmd2 = "cd .. && cd channels && cd tam_mateo && py stream_video_to_macbookpro_server.py"
for channel in channels:
  try:
   cmd =  "cd .. && cd channels && cd "+channel+" && py stream_video_to_windows_server.py"
   process1 = Popen(cmd, shell=True)
  except:
    print("error")