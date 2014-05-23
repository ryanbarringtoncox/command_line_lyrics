# Usage                                                                                                                                                                                
## Dependencies

Depends on Python 2.7 (or later) and lxml.

    sudo pip install lxml

## Install and scrape

For now, script assumes formatting of http://www.songlyrics.com/.  To rip lyrics just clone the repo and cd in.  Then run the script with url arg -

    git clone https://github.com/ryanbarringtoncox/lyric-scraper
    cd lyric-scraper/
    ./lyric-scraper.py http://www.songlyrics.com/mark-mulcahy/the-rabbit-lyrics/

It will scrape the song lyrics and write them to file-in-current-working-dir-like-this.txt.

## Add to your path

Maybe you want to use this script in various directories.  I do.  You can use it anywhere, by adding it to your path like this -

    cd /usr/local/bin
    sudo ln -s /your/path/to/lyric-scraper/lyric-scraper.py ./lyric-scraper
    cd ~
    mkdir rolling-stones-lyrics
    cd rolling-stones-lyrics
    lyric-scraper http://www.songlyrics.com/the-rolling-stones/tumbling-dice-lyrics/
    lyric-scraper http://www.songlyrics.com/the-rolling-stones/rocks-off-lyrics/
    ls

Let me know if you're finding this useful and I'll add compatibility with other lyric websites.  Happy scraping!
