# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeUpdate(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    hash_id = scrapy.Field()
    image = scrapy.Field()
    name_ru = scrapy.Field()
    episode = scrapy.Field()
    translate = scrapy.Field()
