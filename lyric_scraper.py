#!/usr/bin/python
'''
Still waiting on a good lyrics api.  Until then I still want lyrics from the console.
Just run this script the way you'd do a google search for lyrics.  For example -

  ./lyric_scraper beatles in my life

Will get them streaming by on the console.  Boosh!
'''

import requests, sys, urlparse, subprocess
from lxml import html

#domains and elements where lyrics live as key-val.  let's add some more if we can't get all the songs we want.
useable_domains = {'www.metrolyrics.com':'//p[@class="verse"]/text()','www.songlyrics.com':'//p[@id="songLyricsDiv"]/text()'}

def is_valid_url(url):
  """check for page and return it as object if valid"""
  page = requests.get(url)
  if page.status_code != 200:
    return None
  else:
    return page 

def get_args_string():
  """get command line args and return as one concatted string"""
  if len(sys.argv) < 2: sys.exit("Need some args, man!")
  args = sys.argv[1:]
  return ' '.join(arg for arg in args)

def get_domain(url):
  """take full url and return domain"""
  url = url.rstrip('/')
  return urlparse.urlparse(url).hostname

if __name__ == '__main__':
   
  #get args as string, call ruby script, get list of google search results urls
  args_string = get_args_string()
  cmd = "./google_search.rb " + args_string
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
  ruby_response,errors = p.communicate()
  url_list=ruby_response.split('\n')

  #look for useable domains in url list
  useable_urls=[]
  for url in url_list:
    domain = get_domain(url) 
    if domain in useable_domains:
      useable_urls.append(url)

  #check urls for validity and get lyrics if possible
  for url in useable_urls:
    page = is_valid_url(url)
    if page: 
      tree = html.fromstring(page.text)
      target = useable_domains[get_domain(url)]
      lyrics = tree.xpath(target)
      for line in lyrics:
        if line:
          print line.lstrip().rstrip()
      if lyrics:
        #print "found lyrics.  exiting..."
        break #exit for loop if lyrics exist
