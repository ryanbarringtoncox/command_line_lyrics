Usage                                                                                                                                                                                
=======

For now, script assumes formatting of http://www.songlyrics.com/.  To rip lyrics just clone the repo and cd in.

Copy and paste song choice urls into urls.py file list like this -

    urls = [
      "http://www.songlyrics.com/mark-mulcahy/the-rabbit-lyrics/",
      "http://www.songlyrics.com/rem/it-s-the-end-of-the-world-lyrics/",
      "http://www.songlyrics.com/buddy-holly/rock-me-my-baby-lyrics/"
    ]

Then run the script -

    ./word-scraper.py

It will scrape the song lyrics and write them to files in songs dir.

