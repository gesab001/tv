import subprocess
import json
"""
process = "yt-dlp UC-sTAA4sZNqKkDeGK-HOfrw -j -o output.json"
output = subprocess.run(process, stdout=subprocess.PIPE) 
string = json.loads(output.stdout.decode("utf-8"))
with open("output.json", "w") as fp:
   json.dump(string, fp, indent=4)

"""

"""
youtube-dl --get-filename -o "%(upload_date)s, %(title)s, https://www.youtube.com/watch?v=%(UC-sTAA4sZNqKkDeGK-HOfrw)s" "https://www.youtube.com/@ernieknoll"

yt-dlp https://www.youtube.com/@ernieknoll --write-info-json --skip-download

"""
url = input("channel url: ")
process = "yt-dlp "+ url + " --write-info-json --skip-download"
print(process)
proceed = input("continue")

subprocess.call(process, shell=True)
