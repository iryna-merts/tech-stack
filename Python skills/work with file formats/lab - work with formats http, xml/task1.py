import http.client, urllib.parse

anyurl="https://www.awwwards.com/inspiration/image-gallery-canvas-navigation-international-womens-day"
p = urllib.parse.urlparse(anyurl) 
print(p)
print(p[1]) 
print(p[2]+p[3]) 
