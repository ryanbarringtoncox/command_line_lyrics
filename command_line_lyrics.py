#!/usr/bin/python
'''
Still waiting on a good lyrics api.  Until then I still want lyrics from the console.
Just run this script the way you'd do a google search for lyrics.  For example -

  ./command_line_lyrics beatles in my life

Will get them streaming by on the console.  Boosh!

PLEASE DO NOT include double/single quotes or other puncuation in your search string.  Bash doesn't like that.  It will fail.
The eventual goal is to sanitize this on frontend GUI.
'''

import requests, sys, urlparse, subprocess
from lxml import html

#domains and elements where lyrics live as key-val.  let's add some more if we can't get all the songs we want.
useable_domains = {
  'www.metrolyrics.com':'//p[@class="verse"]/text()',
  'www.songlyrics.com':'//p[@id="songLyricsDiv"]/text()',
  'www.lyricsmania.com':'//div[@class="lyrics-body"]/text()',
  'www.azlyrics.com':'//div[@style="margin-left:10px;margin-right:10px;"]/text()'
  }

def is_valid_url(url):
  """Check for page and return as object if valid."""
  page = requests.get(url)
  if page.status_code != 200:
    return None
  else:
    return page 

def get_args_string(args):
  """Get command line args and return as one concatted string."""
  args.append('lyrics') #user shouldn't need to type the word lyrics
  return ' '.join(arg for arg in args)

def get_domain(url):
  """Take full url and return domain."""
  url = url.rstrip('/')
  return urlparse.urlparse(url).hostname

def trim_lyrics(lyrics):
  """Take list of lyric lines, trim beginning empty lines and returns."""
  santized_lyrics = []
  not_found_words = True
  for line in lyrics:
    if not_found_words and line in ['\n','\r\n']:
      continue
    else:
      not_found_words = False
      santized_lyrics.append(line)
  return santized_lyrics

if __name__ == '__main__':
   
  #get args as string, call ruby script, get list of google search results urls
  if len(sys.argv) < 2:
    sys.exit("Need some args, man!")
  args = sys.argv[1:]
  args_string = get_args_string(args)
  cmd = "./google_search.rb " + args_string
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
  ruby_response,errors = p.communicate()
  url_list=ruby_response.split('\n')

  #look for useable domains in url list
  useable_urls=[]
  for url in url_list:
    #print url
    domain = get_domain(url) 
    if domain in useable_domains:
      useable_urls.append(url)

  #check urls for validity and get lyrics if possible
  lyrics = None
  for url in useable_urls:
    page = is_valid_url(url)
    if page: 
      tree = html.fromstring(page.text)
      target = useable_domains[get_domain(url)]
      lyrics = tree.xpath(target)
      if lyrics:
        lyrics = trim_lyrics(lyrics) #trims empty lines from beginning
        reversed_lyrics = trim_lyrics(lyrics[::-1]) #trims empty lines from end
        lyrics = reversed_lyrics[::-1] #reverses reversed lyrics
      for line in lyrics:
        if line:
          print line.lstrip().rstrip()
      if lyrics:
        #print "found lyrics from " + url + " .  exiting..."
        break #exit for loop if lyrics exist
   
  if not lyrics: 
    print "sorry, bud.  couldn't find that one : ("
