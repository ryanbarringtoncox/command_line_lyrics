## Intro

I love the command line.  I love listening to music while I hack.  I love getting the lyrics to songs quickly.  It's a pain to fire up a browser, type a lyrics search into google, wade through the results, copy and paste.  You get the idea.

I spent a few hours trying out a few supposed lyric apis and had no luck.  I want lyrics quick and easy from the command line in one command.  Why not script what I've been doing?

## Dependencies

Depends on Python 2.7 (or later) and lxml library.

    pip install lxml

You'll also need Ruby and ruby-web search.

    gem install ruby-web-search

## Install and scrape 

Clone the repo and cd in -

    git clone https://github.com/ryanbarringtoncox/command_line_lyrics
    cd command_line_lyrics/

Run the script and pass in the words that you'd use to find lyrics online.  Some examples -

    ./lyric_scraper.py the beatles in my life 
    ./lyric_scraper.py buddy holly peggy sue 

And they'll stream by on the console for your reading pleasure.  You can also redirect them to a text file like this -

     ./lyric_scraper.py rolling stones hip shake > hip-shake.txt

