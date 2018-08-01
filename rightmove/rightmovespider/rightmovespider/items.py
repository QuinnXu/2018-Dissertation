# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RightmovespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # house id
    id = scrapy.Field()
    # house price
    price = scrapy.Field()
    # latitude
    lat = scrapy.Field()
    # longitude
    lon = scrapy.Field()
    # brief description
    des = scrapy.Field()
