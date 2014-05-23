#!/usr/bin/python
import requests,sys
from lxml import html
debug=False

# validate args
if len(sys.argv) != 2:
  sys.exit("usage: lyric-scraper http://www.songlyrics.com/mark-mulcahy/the-rabbit-lyrics/")

# get url
url = sys.argv[1]
url=url.rstrip('/')

if debug: print "url is " + url
# dom target, may change in time
target='//p[@id="songLyricsDiv"]/text()'
# remove strings like '(pre-chorus)'
remove_paren_words=True

#get (part of string) between parens and remove
def sliceOutParens(str):
  sub_str=str[str.find("("):str.find(")")+1]
  return str.replace(sub_str,'')

# make sure it's a http://www.valid/url, grab page
try:
  page = requests.get(url)
except:
  sys.exit("Not a valid url.  Exiting...")

# get the text tree
tree = html.fromstring(page.text)
if debug: print tree

# grab desired dom element
lyrics = tree.xpath(target)
if debug: print str(len(lyrics)) + " lines found in element" 
if len(lyrics) == 0:
  print "Url doesn't have songLyricsDiv with words"
  print "  ...exiting"
  sys.exit(2)

# build filename and open
slugs=url.split('/')
filename=slugs[len(slugs)-1]+".txt"
if debug: print "lyrics will be written to " + filename
f=open(filename,"w")

# remove punctuation chars
for line in lyrics:
  if remove_paren_words: line=sliceOutParens(line)
  line=line.lower()
  if line:
    if debug: print line,
    f.write(line)    

f.close()
