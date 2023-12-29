# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NoobItem(scrapy.Item):
    # Define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()

class CatItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()
    screenshot_path = scrapy.Field()
    
class ProItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()
    ai_extract_content = scrapy.Field()
    
class LionItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    directory = scrapy.Field()