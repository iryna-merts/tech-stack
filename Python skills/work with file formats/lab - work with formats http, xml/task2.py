import http.client, urllib.parse, sys
print("Start . . .")
anyurl="https://www.awwwards.com/inspiration/image-gallery-canvas-navigation-international-womens-day"
servername = "www.awwwards.com"
filename = "/inspiration/image-gallery-canvas-navigation-international-womens-day"
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
 with open("awards-file.html","wb") as fsave : 
     fsave.write(reply.read())
 reply.close() 
else:
 print('Error sending request: ', reply.status, " ", reply.reason)
print(". . . ready")

import os
os.startfile("awards-file.html")
pass 

