#!/usr/bin/python
import unittest, command_line_lyrics

class TestLyricScraper(unittest.TestCase):

  def test_print_lyrics(self):
    useable_urls = ['http://www.azlyrics.com/lyrics/beatles/inmylife.html', 'http://www.metrolyrics.com/in-my-life-lyrics-beatles.html']
    command_line_lyrics.print_lyrics(useable_urls)

  def test_find_useable_urls(self):
    urls = ['www.metrolyrics.com/a/path', 'http://trailofsparks.org', 'somefakestuff.com']
    useable_urls = command_line_lyrics.find_useable_urls(urls)
    self.assertGreater(1,len(useable_urls))

  def test_trim_lyrics(self):
    lyrics_oracle = ["Here are lyrics.\n","That are not trimmed.\n","La la la la.\n","\n","\n"]
    untrimmed_lyrics_list = ["\n","\n", "Here are lyrics.\n","That are not trimmed.\n","La la la la.\n","\n","\n"]
    trimmed_lyrics = command_line_lyrics.trim_lyrics(untrimmed_lyrics_list)
    self.assertEquals(trimmed_lyrics,lyrics_oracle)

  def test_get_domain(self):
    url = "https://www.google.com/?gws_rd=ssl#q=lyrics+to+a+cool+song"
    domain = command_line_lyrics.get_domain(url)
    self.assertEquals(domain, "www.google.com")

  def test_get_args_string(self):
    command_line_args = ["buddy","holly","peggy","sue"]
    search_str = command_line_lyrics.get_args_string(command_line_args)
    self.assertEquals(search_str, "buddy holly peggy sue lyrics")

  def test_is_valid_url(self):
    page1 = command_line_lyrics.is_valid_url('http://google.com')
    self.assertTrue(page1!=None)
    page2 = command_line_lyrics.is_valid_url('http://google.com/dagslkeq;lh')
    self.assertFalse(page2!=None)

if __name__ == '__main__':
  unittest.main()
