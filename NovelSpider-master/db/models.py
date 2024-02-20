# 文章信息
from db.ships import major_book, minor_book
from ext import db


class BookModel(db.Model):
    __tablename__ = 't_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    title = db.Column(db.String(256))
    author = db.Column(db.String(256))
    cover = db.Column(db.String(256))
    longIntro = db.Column(db.TEXT)  # 介绍

    latelyFollower = db.Column(db.Integer)
    wordCount = db.Column(db.Integer)
    retentionRatio = db.Column(db.Integer)
    updated = db.Column(db.String)
    isSerial = db.Column(db.BOOLEAN)
    chaptersCount = db.Column(db.Integer)
    lastChapter = db.Column(db.String(256))
    shortIntro = db.Column(db.TEXT)

    major = []
    ship_majors = db.relationship('MajorModel',
                                secondary=major_book,
                                backref=db.backref('t_book', lazy='dynamic'),
                                lazy='dynamic')

    minor = []
    ship_minors = db.relationship('MinorModel',
                                secondary=minor_book,
                                backref=db.backref('t_book', lazy='dynamic'),
                                lazy='dynamic')


    def __init__(self, name, title, author, cover, longIntro,
                 majorCate, minorCate, latefyFollower, wordCount,
                 retentionRatio, updated, isSerial, chaptersCount,
                 lastChapter, shortIntro):
        self.name = name
        self.title = title
        self.author = author
        self.cover = cover
        self.longIntro = longIntro
        self.majorCate = majorCate
        self.minorCate = minorCate
        self.latelyFollower = latefyFollower
        self.wordCount = wordCount
        self.retentionRatio = retentionRatio
        self.updated = updated
        self.isSerial = isSerial
        self.chaptersCount = chaptersCount
        self.lastChapter = lastChapter
        self.shortIntro = shortIntro

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class MinorModel(db.Model):
    __tablename__ = "t_major"
    name = db.Column(db.String(64), primary_key=True)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class MinorModel(db.Model):
    __tablename__ = "t_minor"
    name = db.Column(db.String(64), primary_key=True)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
