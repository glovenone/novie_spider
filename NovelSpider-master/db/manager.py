from db.pymysqlhelper import PyMysqlHelper


class DbManager(object):
    def insert_book(self, book_item):

        select_sql = "select * from t_book where id = %s"
        select_params = (book_item["id"])
        select_result = PyMysqlHelper.getInstance().select_one(select_sql, select_params)
        if select_result == None:
            insert_sql = "insert t_book(id, title, author, grab_time) values (%s, %s, %s, %s)"
            params = (book_item["id"], book_item["title"], book_item["author"], book_item['grab_time'])
            result = PyMysqlHelper.getInstance().insert(insert_sql, params)
            print(result)
        else:
            print("has insert")
        pass

    def update_book(self, book_item):
        pass

    def insert_source(self, source_item):
        insert_sql = "insert t_source(id, book_id, link, website, last_chapter) values (%s,%s,%s,%s,%s)"
        insert_params = (source_item['id'], source_item['book_id'], source_item['link'],
                         source_item['website'], source_item['last_chapter'])
        result = PyMysqlHelper.getInstance().insert(insert_sql, insert_params)
        print(result)

    def insert_chapter(self, chapter_item):
        insert_sql = "insert t_chapter(id, source_id, title, urls, grab_time) values (%s, %s, %s, %s, %s)"
        insert_params = (chapter_item['id'], chapter_item['source_id'], chapter_item['title'],
                         chapter_item['urls'], chapter_item['grab_time'])
        result = PyMysqlHelper.getInstance().insert(insert_sql, insert_params)
        print(result)

    def search_books_for_spider(self, count=100):
        select_sql = "select * from t_book where spider_state = -1"
        select_params = ()
        select_result = PyMysqlHelper.getInstance().select_all(select_sql, select_params)
        return select_result

    def search_book_by_name_and_author(self, name, author):
        select_sql = "select * from t_book where title = %s and author = %s"
        select_params = (name, author)
        select_result = PyMysqlHelper.getInstance().select_one(select_sql, select_params)
        return select_result

    def insert_rank(self, rank_item):
        _sql = "insert t_rank(id, title, short_title, link, type) value (%s, %s, %s, %s, %s)"
        _params = (rank_item['id'], rank_item['title'], rank_item['short_title'],
                   rank_item['link'], rank_item['type'])
        return PyMysqlHelper.getInstance().insert(_sql, _params)

    def insert_rank_book(self, rank_book_item):
        _sql = "insert t_rank_book(id, rank_id, book_id) value (%s, %s, %s)"
        _params = (rank_book_item['id'], rank_book_item['rank_id'], rank_book_item['book_id'])
        return PyMysqlHelper.getInstance().insert(_sql, _params)
