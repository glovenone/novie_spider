import chardet
import requests
from bs4 import BeautifulSoup

from tutorial.spiders.NovelSpider import NovelSpider


class SimpleSpider(object):
    def parse(self, url):
        req = requests.request('GET', url)
        charset = chardet.detect(req.content)

        charsetStr = charset['encoding']
        if charset['encoding'].find('gb2312'):
            charsetStr = 'GBK'

        html = str(req.content, charsetStr)
        soup = BeautifulSoup(html, "html.parser")
        books = soup.find("div", class_='novelslist').findAll('li')
        for book in books:
            name_node = book.find("span", attrs={'class': 's2'})
            name = name_node.a.get_text()
            link = name_node.a.get("href")
            chapter_node = book.find("span", attrs={'class': 's3'})
            chapter_name = chapter_node.a.get_text()
            chapter_link = chapter_node.a.get("href")
            author = book.find("span", attrs={'class': 's4'}).get_text()
            print(name + " " + link + " " + chapter_name + " " + chapter_link + "  " + author)

        next_url = soup.find("div", class_="page").strong.find_next_sibling().get("href")
        print(next_url)

    def parse_detail(self, url):
        req = requests.request('GET', url)
        charset = chardet.detect(req.content)
        charsetStr = charset['encoding']
        if 'GB2312' in charsetStr:
            charsetStr = 'GBK'
        html = str(req.content, charsetStr)
        soup = BeautifulSoup(html, "html.parser")
        cover = soup.find("div", id="fmimg").img.get("src")
        print(cover)
        intro = (soup.find("div", id="intro")).get_text()
        print(intro)

        chapter_nodes = soup.find("div", id="list").findAll("dd")
        for chapter_node in chapter_nodes:
            a = chapter_node.a
            if a:
                chapter_link = chapter_node.a.get("href")
                chapter_name = chapter_node.a.get_text()
                print(chapter_name + "  " + chapter_link)

    def parse_zuihui_search_book_list(self, url):
        req = requests.request('GET', url)
        charset = chardet.detect(req.content)
        charsetStr = charset['encoding']
        if 'GB2312' in charsetStr:
            charsetStr = 'GBK'
        html = str(req.content, charsetStr)
        # print(html)
        soup = BeautifulSoup(html, "html.parser")
        # div_content_node = soup.find("div", class_="content")
        # print(div_content_node)
        books_list_node = soup.find("div", class_="books-list")
        book_nodes = books_list_node.find_all("div", class_="book")
        for book_node in book_nodes:
            name_node = book_node.h4
            name = name_node.get_text()
            author_node = book_node.find("p", class_="author")
            author = author_node.find("span").get_text()
            major = author_node.find("span", class_="cat").get_text()
            link = name_node.a.get("href")
            print(link)

    def parse_zuishu_book_detail(self, url):
        req = requests.request('GET', url)
        charset = chardet.detect(req.content)
        charsetStr = charset['encoding']
        if 'GB2312' in charsetStr:
            charsetStr = 'GBK'
        html = str(req.content, charsetStr)
        # print(html)
        soup = BeautifulSoup(html, "html.parser")

        book_info_node = soup.find("div", "book-info")
        cover = book_info_node.img.get("src")

        p_sup_text = book_info_node.find("p", "sup").get_text()

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

        book_data_i_value_nodes = soup.find("div", "book-data").find_all("i", "value")
        if len(book_data_i_value_nodes) >= 2:
            total_reader = book_data_i_value_nodes[0].get_text()
            retentionRatio = book_data_i_value_nodes[1].get_text()
        else:
            total_reader = book_data_i_value_nodes[0].get_text()
            retentionRatio = "32.79%"

        content_intro_node = soup.find("p", "content intro")
        intro = content_intro_node.get_text()


    def request_html(self, url):
        req = requests.request('GET', url)
        charset = chardet.detect(req.content)
        charsetStr = charset['encoding']
        if 'GB2312' in charsetStr:
            charsetStr = 'GBK'
        html = str(req.content, charsetStr)
        return html

    def parse_book_chapters(self, url):
        """
        解析单独书籍的章节
        :param url:
        :return:
        """
        html = self.request_html(url)





if __name__ == '__main__':
    spider = NovelSpider()
    spider
