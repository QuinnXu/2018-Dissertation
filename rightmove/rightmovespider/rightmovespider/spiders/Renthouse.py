from scrapy import  Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from rightmovespider.items import RightmovespiderItem
from scrapy.linkextractors import LinkExtractor

class Renthouse(CrawlSpider):
    name = 'rent_price'
    allowed_domains = ['rightmove.co.uk']
    urllist = []
    for i in range(0,1000,24):
        url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1019&index='+str(i)
        urllist.append(url)

    start_urls = urllist

    rules = (
        Rule(LinkExtractor(allow=('/property-to-rent/find\.html\?locationIdentifier=REGION%5E1019&index=\d+',),
                           )),
        Rule(LinkExtractor(allow=('/property-to-rent/property-\d+'),),
             callback="info_page")
    )
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def info_page(self, response):

        print('进入页面')

        item = RightmovespiderItem()

        item['id'] = response.xpath('//div[@class ="clearfix main"]/script[3]'
                                    ).re(r'propertyId":(\d+),"viewType')[0]
        item['des'] = response.xpath('//title/text()')[0].extract()

        item['lat'] = response.xpath('//div[@class ="clearfix main"]/script[3]'
                                     ).re(r'latitude":(\d.+),"longitude')
        item['lon'] = response.xpath('//div[@class ="clearfix main"]/script[3]'
                                     ).re(r'longitude":(-\d.+)\},"')
        price = ''.join(response.xpath('//p [@class="property-header-price "]/strong/text()'
                               ).re(r'(\d)'))
        tag = response.xpath('//p [@class="property-header-price "]/strong/text()'
                             )[0].extract()[-3:]
        if tag == ' pw':
            item['price'] = str(4 * int(price))
        else:
            item['price'] = price

        yield item

