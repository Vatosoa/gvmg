# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GvmgItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    date = scrapy.Field()
    place = scrapy.Field()
    author = scrapy.Field()
    translator = scrapy.Field()
    title = scrapy.Field()
    text_content = scrapy.Field()