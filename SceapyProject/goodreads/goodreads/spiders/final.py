import scrapy
import re
from ..items import GoodreadsItem
# import urlib.parse
from urllib.parse import urljoin
# from goodreads.items import GoodreadsItem

# from urlparse import urlparse
from scrapy.linkextractors import LinkExtractor
k=input("input the bok to be searched ")
k=k.replace(" ","+")
#print(k)

url='https://www.goodreads.com/search?utf8=✓&q='+k+'&search_type=books'
print(url)
class BooksToScrape(scrapy.Spider):

    name='genreBot'
    start_urls=[
        url
    ]


    def parse(self, response):
        self.item=GoodreadsItem()
        # item=MyItem()
        # item['main_url']=response.url
        idtag=response.css(".u-anchorTarget").extract_first()
        # yield{'titletext':idtag}
        m = re.search('id="(.+?)" class', idtag).group(1)
        print(m)
        k=m
        url1="https://www.goodreads.com/book/show/"
        new_url=urljoin(url1,str(k))
        # item['new_url']=response.url
        url=new_url

        #return scrapy.Request(url1, callback=self.parse_genre)
        request1 = scrapy.Request(url, callback=self.parse_genre)
        #request.meta['item']=item

        self.item['url'] = url
        return request1


    def parse_genre(self,response):
        #item=response.meta['item']
        self.item=GoodreadsItem()
        genre = response.css(".left .bookPageGenreLink").extract()
        # print(genre)
        # return requests

        #  m = re.search('">(^\w+?)</a',genre).group(1)
        # print(m)
        gl=list()
        # s=genre
        for s in genre:
            start = s.find('">') + 2
            end = s.find('</', start)
            g=s[start:end]
            # print(str(g))
            gl.append(g)
            print(g)
        #return gl
        #self.item['gl']=gl[0]
        #yield items
        #yield item
        #return item

