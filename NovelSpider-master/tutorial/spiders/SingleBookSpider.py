import hashlib

import scrapy
import time
from bs4 import BeautifulSoup
from scrapy import Request

from tutorial.items import BookItem, SourceItem, ChapterItem
from utils.md5_util import md5_util
from utils.time_util import current_milli_time


class SingleBookSpider(scrapy.Spider):
    name = 'hunhun520'
    allowed_domains = ['www.hunhun520.com',
                       'www.zhuishushenqi.com']

    def start_requests(self):
        urls = [
            'https://www.hunhun520.com/shuku/0_0_0_0_0_0_0_0_1233.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 解析列表页中的所有书籍url并交给scrapy下载后并进行解析
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        books = soup.find("div", "novelslist").findAll('li')
        for book in books:
            name_node = book.find("span", 's2')
            book_name = name_node.a.get_text()
            source_link = name_node.a.get("href")
            author = book.find("span", "s4").get_text()
            last_chapter = book.find("span", "s3").a.get_text()

            book_id = md5_util(str(book_name + author))
            source_id = md5_util(str(source_link))

            book_item = BookItem()
            book_item['id'] = book_id
            book_item['title'] = book_name
            book_item['author'] = author
            book_item['grab_time'] = current_milli_time()
            book_item['cover'] = ""
            book_item['intro'] = ""
            book_item['major'] = ""
            book_item['minor'] = ""
            book_item['total_words'] = ""
            book_item['total_reader'] = ""
            book_item['retentionRatio'] = ""

            source_item = SourceItem()
            source_item['id'] = source_id
            source_item['link'] = source_link
            source_item['website'] = self.name
            source_item['last_chapter'] = last_chapter
            source_item['book_id'] = book_id
            yield source_item

            # 抓取追书神器网站上的内容
            # zuishui_search_url = "http://www.zhuishushenqi.com/search?val=" + book_name
            # yield Request(zuishui_search_url, meta={"book_item": book_item},
            #               callback=self.parse_zuishu_search_book_list)

        # 解析章节列表
        yield Request(source_link, meta={"source_id": source_id, 'bookItem': book_item}, callback=self.parse_detail,
                      dont_filter=False)

        # 抓取下一页
        next_url = soup.find("div", class_="page").strong.find_next_sibling().get("href")
        yield Request(next_url, callback=self.parse, dont_filter=False)

    def parse_detail(self, response):
        '''
        解析书籍封面 推荐 章节
        :param response:
        :return:
        '''
        bookItem = response.meta['bookItem']
        source_id = response.meta['source_id']

        data = response.body
        soup = BeautifulSoup(data, "html.parser")

        # 解析书籍封面
        book_detail_node = soup.find('div', id='maininfo')
        cover = book_detail_node.find('div', id='fmimg').img.get('src')
        bookItem['cover'] = cover
        yield bookItem

        chapter_nodes = soup.find("div", id="list").findAll("dd")
        for chapter_node in chapter_nodes:
            a = chapter_node.a
            if a:
                chapter_link = chapter_node.a.get("href")
                chapter_name = chapter_node.a.get_text()

                chapter_item = ChapterItem()
                chapter_item['id'] = md5_util(str(chapter_link))
                chapter_item['title'] = chapter_name
                chapter_item['urls'] = chapter_link
                chapter_item['source_id'] = source_id
                chapter_item['grab_time'] = current_milli_time()
                yield chapter_item

    def parse_zuishu_search_book_list(self, response):
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
                yield Request(full_url, meta={"book_item": book_item}, callback=self.parse_zhuishu_book_detail,
                              dont_filter=False)
                break

    def parse_zhuishu_book_detail(self, response):
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
