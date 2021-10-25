import urllib.request
import os


f = open("html_files/gitusers" + ".html", "wb")
response = urllib.request.urlopen("http://45.79.253.243/index.html/")
html = response.read()
f.write(html)
f.close()

