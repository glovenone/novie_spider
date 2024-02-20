# # scrapy api
# from scrapy import signals, log
# from twisted.internet import reactor
# from scrapy.crawler import Crawler
# from scrapy.settings import Settings
#
# from db.manager import DbManager
# from tutorial.spiders.ZhuishuSpider import ZhuishuSpider
#
#
# def spider_closing(spider):
#     """Activates on spider closed signal"""
#     log.msg("Closing reactor", level=log.INFO)
#     reactor.stop()
#
#
#
#
# log.start(loglevel=log.DEBUG)
# settings = Settings()
# # crawl responsibly
# settings.set("USER_AGENT",
#              "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
# crawler = Crawler(settings)
# # stop reactor when spider closes
# crawler.signals.connect(spider_closing, signal=signals.spider_closed)
# crawler.configure()
#
# spider = ZhuishuSpider()
# db = DbManager()
# items = db.search_books_for_spider(100)
# wait_urls = []
# for item in items:
#     wait_urls.append(item['url'])
#
# crawler.crawl(ZhuishuSpider())
# crawler.start()
# reactor.run()
