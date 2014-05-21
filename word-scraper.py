#!/usr/bin/python
from lxml import html
import requests,sys

debug=True
#url="http://www.songlyrics.com/mark-mulcahy/i-taketh-away-lyrics/"
#url="http://www.songlyrics.com/mark-mulcahy/the-rabbit-lyrics/"
#url="http://www.songlyrics.com/mark-mulcahy/poison-candy-heart-lyrics/"
url=sys.argv[1]
if debug: print "url is " + url
target='//p[@id="songLyricsDiv"]/text()'
# remove strings like '(pre-chorus)'
remove_paren_words=True
remove_verse_lines=True #remove lines that start with string "verse"

#get (part of string) between parens and remove
def sliceOutParens(str):
  sub_str=str[str.find("("):str.find(")")+1]
  return str.replace(sub_str,'')

# grab webpage and get the text tree
page = requests.get(url)
tree = html.fromstring(page.text)
if debug: print tree

slugs=url.split('/')
filename=slugs[len(slugs)-2]+".txt"
if debug: print "lyrics will be written to " + filename
f=open(filename,"w")

# grab desired dom element
lyrics = tree.xpath(target)
if debug: print str(len(lyrics)) + " lines found in element" 
if len(lyrics) == 0:
  print "Damn.  This is one of those annoyingly empthy urls."
  print "  ...exiting"
  sys.exit(2)

# remove punctuation chars
for line in lyrics:
  if remove_paren_words: line=sliceOutParens(line)
  # come back to following in if it's a consistent issue...
  #if remove_verse_lines and line[0:5]=='verse': break
  line=line.replace('"','').replace('\'','').replace('.','').replace(',','').strip('\n').lower()
  if line:
    if debug: print line,
    f.write(line)    

f.close()
