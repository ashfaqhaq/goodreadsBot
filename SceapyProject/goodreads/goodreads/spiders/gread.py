import scrapy
import re
from scrapy.linkextractors import LinkExtractor
#k=input()
#k=k.replace(" ","+")
#print(k)
url='https://www.goodreads.com/search?utf8=✓&q=database+system+concepts&search_type=books'
#url='https://www.goodreads.com/search?utf8=✓&q='+k+'&search_type=books'
class BooksToScrape(scrapy.Spider):
    name='books'
    start_urls=[
        url
    ]
    def  parse(self, response):
        idtag=response.css(".u-anchorTarget").extract_first()
        yield{'titletext':idtag}
        m = re.search('id=(.+?) class', idtag).group(1)
        k=m
        print(k)
        print(url)
