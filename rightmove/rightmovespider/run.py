import sys
import scrapy.cmdline

# sys.exit(scrapy.cmdline.execute('scrapy startproject rightmovespider'.split()))

scrapy.cmdline.execute('scrapy crawl rent_price -o property_info_0801_2.csv'.split())