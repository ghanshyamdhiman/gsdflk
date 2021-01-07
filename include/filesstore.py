from webscrapper import LyricsScrapper

the_url = "http://www.values.com/inspirational-quotes"

the_scrapper = LyricsScrapper(the_url)

the_lyrics_data = the_scrapper.get_lyics()

def store_the_file(file_name, lyrics_data):
    try:
       f = open(file_name, "a")
       f.write(lyrics_data)
    finally:
       f.close()
   
the_file_name = "test_file.txt"

store_the_file(the_file_name, the_lyrics_data)
