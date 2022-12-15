import json

f = open("channels.json", "r")
jsondata = json.loads(f.read())
print(jsondata)