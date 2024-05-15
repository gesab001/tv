import os
import subprocess

channels = os.listdir("channels")

print("SELECT CHANNEL TO STREAM")
for channel in range(1, len(channels)+1):
   print(str(channel) + ". " + channels[channel-1] )

selected_channel = int(input("channel: ")) -1
channel_folder = channels[selected_channel]
print(channel_folder)

command = "cd channels && cd " + channel_folder + " && py stream_video_to_macbookpro_server.py"
subprocess.call(command, shell=True)