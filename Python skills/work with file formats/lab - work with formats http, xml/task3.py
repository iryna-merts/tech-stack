import http.client, urllib.parse, sys
print("Start . . .")
anyurl="http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/data/courses/reed.xml"
servername = "aiweb.cs.washington.edu"
filename = "/research/projects/xmltk/xmldata/data/courses/reed.xml"
try:
 server = http.client.HTTPSConnection(servername) 
 server.request('GET', filename) 
 reply = server.getresponse() 
except: 
 info= sys.exc_info() 
 print("Error HTTPSConnection:\n", info[0], info[1])
 sys.exit() 
print(". . . reply . . .") 
if reply.status == 200: 
 with open("edu-file.xml","wb") as fsave :
     fsave.write(reply.read()) 
 reply.close()
else:
 print('Error sending request: ', reply.status, " ", reply.reason)
print(". . . ready")

import os
os.startfile("edu-file.xml")
pass 

