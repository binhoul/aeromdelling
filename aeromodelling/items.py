# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class AeromodellingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    postTitle = Field()
    postId = Field()
    postUrl = Field()
    postDate = Field()
    postAuthor = Field()
    postText = Field()
    repostCount = Field()

class ImageItem(scrapy.Item):
   imgUrl = Field()
   images = Field()
