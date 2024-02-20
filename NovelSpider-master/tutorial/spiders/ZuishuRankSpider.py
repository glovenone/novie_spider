import hashlib
import json

import scrapy
import time
from bs4 import BeautifulSoup
from scrapy import Request

from db.manager import DbManager
from tutorial.items import BookItem, SourceItem, ChapterItem, RankItem, RankBookItem
from utils.md5_util import md5_util
from utils.time_util import current_milli_time


class ZhuishuRankSpider(scrapy.Spider):
    name = 'zhuishuRank'
    allowed_domains = ['zhuishushenqi.com']

    def start_requests(self):
        urls = [
            'http://api.zhuishushenqi.com/ranking/gender'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 解析列表页中的所有书籍url并交给scrapy下载后并进行解析
        data = json.loads(response.body_as_unicode())
        male_ranks = data['male']  # str(data).json()['male']
        female_ranks = data['female']  # .json()['female']
        for rank in male_ranks:
            print(rank)
            rank_link = 'http://api.zhuishushenqi.com/ranking/' + rank['_id'] + "?type=male"
            rank_item = RankItem()
            rank_item['id'] = rank['_id']
            rank_item['title'] = rank['title']
            rank_item['short_title'] = rank['shortTitle']
            rank_item['link'] = rank_link
            rank_item['type'] = 'male'
            yield rank_item
            # 解析章节列表
            yield Request(rank_link, meta={"rank_id": rank['_id']}, callback=self.parse_rank_books, dont_filter=False)

        for rank in female_ranks:
            print(rank)
            rank_link = 'http://api.zhuishushenqi.com/ranking/' + rank['_id'] + "?type=female"
            rank_item = RankItem()
            rank_item['id'] = rank['_id']
            rank_item['title'] = rank['title']
            rank_item['short_title'] = rank['shortTitle']
            rank_item['link'] = rank_link
            rank_item['type'] = 'female'
            yield rank_item
            # 解析章节列表
            yield Request(rank_link, meta={"rank_id": rank['_id']}, callback=self.parse_rank_books, dont_filter=False)

    def parse_rank_books(self, response):
        rank_id = response.meta['rank_id']
        data = json.loads(response.body_as_unicode())
        result = data  # str(data).json()
        ok = result['ok']

        books = result['ranking']['books']

        for book in books:
            print(book)
            self.handle_rank_book_item(book, rank_id)

    def handle_rank_book_item(self, book, rank_id):
        title = book['title']
        author = book['author']

        db = DbManager()
        book = db.search_book_by_name_and_author(title, author)
        if book is not None:
            rank_book_item = RankBookItem()
            rank_book_item['rank_id'] = rank_id

            rank_book_item['book_id'] = book['id']
            yield rank_book_item
