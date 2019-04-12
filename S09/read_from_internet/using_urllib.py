# source : https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
import re
import urllib.request


url = "http://www.python.org"

with urllib.request.urlopen(url) as f:
    mybytes = f.read()

mystr = mybytes.decode("utf8")


with open("output.html", 'w') as fw:
    fw.write(mystr)

