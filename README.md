# Usage                                                                                                                                                                                
## Intro

I love the console.  I love listening to music while I hack.  I love get the lyrics to songs quickly.  It's a pain to fire up a browser, type a lyrics search in google, wade through the results, copy and paste.  Blah blah.

I spent a few hours trying out a few supposed lyric apis and had no luck.  Why not script what I've been doing so I can get lyrics quickly, from the command line, with one line?

## Dependencies

Depends on Python 2.7 (or later) and lxml library.

    sudo pip install lxml

You'll also need Ruby and ruby-web search.

    sudo gem install ruby-web-search

## Install and scrape 

Clone the repo and cd in -

    git clone https://github.com/ryanbarringtoncox/lyric_scraper
    cd lyric_scraper/

Run the script and pass in the words that you'd use to find lyrics online.  Some examples -

    ./lyric_scraper.py the beatles in my life lyrics
    ./lyric_scraper.py buddy holly peggy sue lyrics

And they'll stream by on the console for your reading pleasure.  You can also redirect them to a text file like this -

     ./lyric_scraper.py rolling stones hip shake lyrics > hip-shake.txt

## Add to your path

Maybe you want to use this script in various directories.  I do.  You can use it anywhere, by adding it to your path like this -

    cd /usr/local/bin
    sudo ln -s /your/path/to/lyric_scraper/lyric_scraper.py ./lyric_scraper
    cd ~
    mkdir rolling-stones-lyrics
    cd rolling-stones-lyrics
    ./lyric_scraper.py sweet jane velvet underground lyrics > sweet-jane.txt
    ls
    cat sweet-jane.txt
