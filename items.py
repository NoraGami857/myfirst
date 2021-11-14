# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    #info = scrapy.Field()#简介
    # score = scrapy.Field()#分数
    # comment = scrapy.Field()#评论

    pass
