# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class DospItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    journal = Field()
    date_journal = Field()
    book_name = Field()
    page_number = Field()
    title = Field()
    page_text = Field()
    url = Field()
    date_scraped = Field()
    pass
