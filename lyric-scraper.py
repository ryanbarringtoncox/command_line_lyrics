#!/usr/bin/python
import requests,sys
from lxml import html

debug=False
url = sys.argv[1]

if debug: print "url is " + url
# dom target, may change in time
target='//p[@id="songLyricsDiv"]/text()'
# remove strings like '(pre-chorus)'
remove_paren_words=True

#get (part of string) between parens and remove
def sliceOutParens(str):
  sub_str=str[str.find("("):str.find(")")+1]
  return str.replace(sub_str,'')

# grab webpage and get the text tree
page = requests.get(url)
tree = html.fromstring(page.text)
if debug: print tree

url=url.rstrip('/')
slugs=url.split('/')
filename=slugs[len(slugs)-1]+".txt"
if debug: print "lyrics will be written to " + filename
f=open(filename,"w")

# grab desired dom element
lyrics = tree.xpath(target)
if debug: print str(len(lyrics)) + " lines found in element" 
if len(lyrics) == 0:
  print "Invalid url.  Or url contains no words in <div id='songLyricsDiv'></div>"
  print "  ...exiting"
  sys.exit(2)

# remove punctuation chars
for line in lyrics:
  if remove_paren_words: line=sliceOutParens(line)
  line=line.lower()
  if line:
    if debug: print line,
    f.write(line)    

f.close()
