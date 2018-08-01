from scrapy import Request
from scrapy.spiders import Spider
from rightmovespider.items import RightmovespiderItem


class Onepage(Spider):
    name = 'onepage'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.rightmove.co.uk/property-to-rent/property-70138781.html'
        yield Request(url, headers=self.headers)

    def parse_item(self, response):
        item = RightmovespiderItem()
        item['id'] = response.xpath('//div[@class ="clearfix main"]/script[3]'
                                    ).re(r'propertyId":(\d+),"viewType')[0]
        item['des'] = response.xpath('//title/text()')[0].extract()

        item['lat'] = response.xpath('//div[@class ="clearfix main"]/script[3]'
                                          ).re(r'latitude":(\d.+),"longitude')
        item['lon'] = response.xpath('//div[@class ="clearfix main"]/script[3]'
                                     ).re(r'longitude":(-\d.+)\},"')
        price = response.xpath('//p [@class="property-header-price "]/strong/text()'
                                       ).re(r'(\d+)')[0]
        tag = response.xpath('//p [@class="property-header-price "]/strong/text()'
                                       )[0].extract()[-3:]
        if tag == ' pw':
            item['price'] = str(4*int(price))
        else:
            item['price'] = price

        yield item