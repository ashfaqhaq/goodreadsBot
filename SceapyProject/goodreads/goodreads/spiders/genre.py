import scrapy
import re

from scrapy.linkextractors import LinkExtractor
#k=input()
#k=k.replace(" ","+")
#print(k)
#static_url='https://www.goodreads.com/search?utf8=✓&q=database+system+concepts&search_type=books'
# url='https://www.goodreads.com/search?utf8=✓&q='+k+'&search_type=books'
url = "https://www.goodreads.com/book/show/161332.Database_System_Concepts"
class BooksToScrape(scrapy.Spider):
    name='booksa'
    start_urls=[
        url
    ]
    def  parse(self, response):
        genre=response.css(".left .bookPageGenreLink").extract()
        yield{'titletext':genre}
        # m = re.search('n">(^\w+?)</a',genre).group(1)
        # print(m)
        # s=genre
        for s in genre:

            start=s.find('">')+2
            end=s.find('</',start)
            print(s[start:end])
        # print(m)
        #for a in genre:
        #    m = re.search('>(.+?)<',genre).group(1)
        #         #   k=m
        #         #   print(k)
        #         #    # print(url)