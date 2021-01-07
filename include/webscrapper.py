import requests 
from bs4 import BeautifulSoup 

class LyricsScrapper:
  def __init__(self, website_url):
    self.weburl = website_url
    
  def get_lyrics(self):
    r = requests.get(self.weburl)   
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup.prettify()
