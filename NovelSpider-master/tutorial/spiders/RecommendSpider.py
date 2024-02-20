import hashlib

import scrapy
import time
from bs4 import BeautifulSoup
from scrapy import Request

from tutorial.items import BookItem, SourceItem, ChapterItem
from utils.md5_util import md5_util
from utils.time_util import current_milli_time


class RecommendSpider(scrapy.Spider):
    name = 'recommend'
    allowed_domains = ['www.hunhun520.com']

    wait_urls = []

    def start_requests(self):
        urls = self.wait_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.body
        book_item = response.meta['book_item']
        soup = BeautifulSoup(data, "html.parser")

        books_list_node = soup.find("div", class_="books-list")
        book_nodes = books_list_node.find_all("div", class_="book")
        for book_node in book_nodes:
            name_node = book_node.h4
            name = "".join(name_node.get_text().split())
            author_node = book_node.find("p", class_="author")
            author = author_node.find("span").get_text()
            if author == book_item['author'] and name == book_item['title']:
                major = author_node.find("span", class_="cat").get_text()
                book_item['major'] = major
                link = name_node.a.get("href")
                full_url = response.urljoin(link)
                yield Request(full_url, meta={"book_item": book_item}, callback=self.parse_detail,
                              dont_filter=False)
                break

    def parse_detail(self, response):
        book_item = response.meta['book_item']
        data = response.body
        soup = BeautifulSoup(data, "html.parser")

        book_info_node = soup.find("div", "book-info")
        cover = book_info_node.img.get("src")
        book_item['cover'] = cover

        p_sup_text = book_info_node.find("p", "sup").get_text()

        minor = ""
        total_words = "未统计"
        values = p_sup_text.split("|")
        if len(values) == 3:
            minor = values[1]
            total_words = values[2]
        elif len(values) == 2:
            minor = values[1]
            total_words = "未统计"
        else:
            minor = ""
            total_words = "未统计"
        book_item['minor'] = minor
        book_item['total_words'] = total_words

        book_data_i_value_nodes = soup.find("div", "book-data").find_all("i", "value")
        total_reader = ""
        retentionRatio = ""
        if len(book_data_i_value_nodes) >= 2:
            total_reader = book_data_i_value_nodes[0].get_text()
            retentionRatio = book_data_i_value_nodes[1].get_text()
        else:
            total_reader = book_data_i_value_nodes[0].get_text()
            retentionRatio = "32.79%"
        book_item['total_reader'] = total_reader
        book_item['retentionRatio'] = retentionRatio

        content_intro_node = soup.find("p", "content intro")
        intro = content_intro_node.get_text()
        book_item['intro'] = intro
        yield book_item