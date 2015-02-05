#!/usr/bin/python
import unittest, command_line_lyrics

class TestLyricScraper(unittest.TestCase):

  def test_is_valid_url(self):
    page1 = command_line_lyrics.is_valid_url('http://google.com')
    self.assertTrue(page1!=None)
    page2 = command_line_lyrics.is_valid_url('http://google.com/dagslkeq;lh')
    self.assertFalse(page2!=None)

if __name__ == '__main__':
  unittest.main()
