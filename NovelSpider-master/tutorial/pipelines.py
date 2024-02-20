# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql

from db.manager import DbManager
from tutorial.items import BookItem, SourceItem, ChapterItem, RankItem, RankBookItem


class TutorialPipeline(object):
    dbManager = DbManager()

    def __init__(self):
        # 可选实现，做参数初始化等
        pass

    def open_spider(self, spider):
        # self.fp = open("book", 'w')
        pass

    def close_spider(self, spider):
        # self.fp.close()
        pass

    def process_item(self, item, spider):
        # j = json.dumps(item._dict_())
        # print(item)

        if isinstance(item, BookItem):
            self.dbManager.insert_book(item)
        elif isinstance(item, SourceItem):
            self.dbManager.insert_source(item)
        elif isinstance(item, ChapterItem):
            self.dbManager.insert_chapter(item)
        elif isinstance(item, RankItem):
            self.dbManager.insert_rank(item)
        elif isinstance(item, RankBookItem):
            self.dbManager.insert_rank_book(item)

        # if isinstance(item, BookItem):
        #     # connection = pymysql.connect(host='127.0.0.1',
        #     #                              user='root',
        #     #                              password='root',
        #     #                              db='NovelDb',
        #     #                              charset='utf8',
        #     #                              cursorclass=pymysql.cursors.DictCursor)
        #     # cursor = connection.cursor()
        #     _args = (item['id'],
        #              item['name'],
        #              item['author'],
        #              item['cover'],
        #              item['intro'],
        #              item['major'],
        #              item['minor'],
        #              item['total_words'],
        #              item['total_reader'],
        #              item['retentionRatio'])
        #
        #     _sql = """
        #             INSERT INTO t_book (
        #             id,name,author,cover,intro,major,minor,total_words,total_reader,retentionRatio) VALUES
        #             (%s,%s,%s, %s, %s,%s, %s,%s, %s,%s)"""
        #
        #     db_helper(_sql, _args)
        #     # connection.commit()
        #     # book = insertOrUpdate(db_config['local'], _sql, _args)
        #
        #     # j = json.dumps(item)
        #     # print(book)
        #     # self.fp.write(j)
        #
        # elif isinstance(item, SourceItem):
        #     _args = (item['id'],
        #              item['book_id'],
        #              item['link'],
        #              item['last_chapter'],
        #              item['website'])
        #
        #     _sql = """INSERT INTO t_source (
        #                         id,book_id,link,last_chapter,website) VALUES
        #                         (%s,%s,%s, %s, %s)"""
        #     db_helper(_sql, _args)
        # elif isinstance(item, ChapterItem):
        #     _args = (item['id'],
        #              item['source_id'],
        #              item['title'],
        #              item['url'])
        #
        #     _sql = """INSERT INTO t_chapter (id,source_id,title,url) VALUES (%s,%s,%s, %s)"""
        #     db_helper(_sql, _args)
        return item

# def db_helper(sql, args):
#     connection = pymysql.connect(host='127.0.0.1',
#                                  user='root',
#                                  password='root',
#                                  db='NovelDb',
#                                  charset='utf8',
#                                  cursorclass=pymysql.cursors.DictCursor)
#     cursor = connection.cursor()
#     cursor.execute(sql, args)
#     connection.commit()
