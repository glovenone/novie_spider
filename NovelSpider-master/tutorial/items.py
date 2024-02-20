# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    id = scrapy.Field()  # id有name+author md5()计算得来
    title = scrapy.Field()
    author = scrapy.Field()
    cover = scrapy.Field()
    intro = scrapy.Field()
    major = scrapy.Field()
    minor = scrapy.Field()
    total_words = scrapy.Field()
    total_reader = scrapy.Field()
    retentionRatio = scrapy.Field()
    grab_time = scrapy.Field()
    complete = scrapy.Field()


class SourceItem(scrapy.Item):
    id = scrapy.Field()  # id有url md5()计算得来
    book_id = scrapy.Field()
    link = scrapy.Field()
    last_chapter = scrapy.Field()
    website = scrapy.Field()


class ChapterItem(scrapy.Item):
    id = scrapy.Field()  # id有url md5()计算得来
    source_id = scrapy.Field()
    title = scrapy.Field()
    urls = scrapy.Field()
    grab_time = scrapy.Field()


class RankItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    short_title = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()  # type： male female


class RankBookItem(scrapy.Item):
    id = scrapy.Field()
    rank_id = scrapy.Field()
    book_id = scrapy.Field()
