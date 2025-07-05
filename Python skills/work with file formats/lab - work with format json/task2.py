destfile = "res-file.json"
import os
import subprocess
dirname = os.path.abspath('.') 
filename = os.path.join(dirname, destfile)
parprog = subprocess.Popen(["notepad.exe", filename])
