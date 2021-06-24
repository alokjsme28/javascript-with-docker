#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
import subprocess

f = cgi.FieldStorage()
cmd1 = f.getvalue("x")

out = "sudo " +cmd1
output = subprocess.getoutput(out)
print(output)
