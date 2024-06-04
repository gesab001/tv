import cgi
import cgitb
import json
import os
import subprocess

cgitb.enable()

form = cgi.FieldStorage()

#keyword = form.getvalue('keyword')

command = "py ../get_channels.py"
subprocess.call(command) 
print("Content-Type: application/json;charset=utf-8\n")
print("Success")
