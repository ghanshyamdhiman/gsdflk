import requests 
from bs4 import BeautifulSoup 

class LyricsScrapper:
  def __init__(self, website_url):
    self.weburl = website_ul
    
  def get_lyrics(self):
    r = requests.get(URL)   
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup.prettify()
