# links:
# https://support.oneskyapp.com/hc/en-us/article_attachments/202761727/example_2.json

import urllib.request

remoteaddr = "https://support.oneskyapp.com/hc/en-us/article_attachments/202761727/example_2.json"
destfile = "res-file.json" 

remotefile = urllib.request.urlopen(remoteaddr)

with open(destfile,"w") as fsave : 
 fsave.write(remotefile.read().decode(encoding='utf-8'))
remotefile.close()
