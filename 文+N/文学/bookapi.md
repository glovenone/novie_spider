

接口地址：http://ab-dev.y5en.com/brs-app/brs.sec

一、书籍列表
1.榜单推荐
pid:001001

param:

参数	数据类型	是否必填	说明
channel	int	是	频道，推荐-0 男生-1 女生-2
type	int	否	榜单类型，推荐榜-0  完本榜-1 番茄榜(付费榜)-2  黑马榜-3
limit	int	否	数据条数，默认8
qt	int	否	随机请求次数，每次请求自增1 


{
    "retCd": 0, 
    "retMsg": "string", 
    "data": [
        {
                        "type": 0, 
                        "title": "推荐", 
                        "items": [
                            {
                                "id": 0, 
                                "name": "神医庶女", 
                                "cover": "http://www.baidu.com", 
                                "cates": [
                                   "玄幻"
                                ], 
                                "tags": [
                                    "标签"
                                ], 
                                "finishState": 1, 
                                "score": "10", 
                                "popVal": "2131", 
                                "hotVal": "1231", 
                                "fansVal": "1231", 
                                "desc": "很好看"
                            }
                        ]
                    
        }
    ]
}


2.个性推荐（猜你喜欢）
pid:001002

param:

参数	数据类型	是否必填	说明
channel	int	是	频道，推荐-0 男生-1 女生-2
pageNo	int	是	数据页数，起始1


{
    "retCd": 0,  
    "retMsg": "string", 
    "data": [
        {
            "id": 0, 
            "name": "神医庶女", 
            "cover": "http://www.baidu.com", 
            "cates": [
                "玄幻"    
            ], 
            "tags": [
                "标签"
            ], 
            "finishState": 1, 
            "score": "10", 
            "popVal": "2131", 
            "hotVal": "1231", 
            "fansVal": "1231", 
            "desc": "很好看"
        }
    ]
}




3.编辑推荐（最新上架）
pid:001003

param:

参数	数据类型	是否必填	说明
channel	int	是	频道，推荐-0 男生-1 女生-2
type	int	否	推荐类型，专属推荐-10  口碑精选-11 新晋都市-12 新晋玄幻-13 新晋现言-14 新晋古言-15
limit	int	否	数据条数，默认8
qt	int	否	随机请求次数，每次请求自增1 


{
    "retCd": 0,  
    "retMsg": "string", 
    "data": [
        {
            "type": 1, 
            "title": "专属推荐", 
            "items": [
                {
                    "id": 0, 
                    "name": "神医庶女", 
                    "cover": "http://www.baidu.com", 
                    "cates": [
                        "玄幻"
                    ], 
                    "tags": [
                        "标签"
                    ], 
                    "finishState": 1, 
                    "score": "10", 
                    "popVal": "2131", 
                    "hotVal": "1231", 
                    "fansVal": "1231", 
                    "desc": "很好看"
                }
            ]
        }
    ]
}


二、书籍信息
1.书籍详情
pid:002001

param:

参数	数据类型	是否必填	说明
bookId	string	是	书籍id


{
    "retCd": 0, 
    "retMsg": "string", 
    "data": {
        "id": 0, 
        "name": "神医庶女", 
        "cover": "http://www.baidu.com", 
        "cates": [
            "玄幻"
        ], 
        "tags": [
            "标签"
        ], 
        "finishState": 1, 
        "score": 1.11, 
        "readVal": 1, 
        "hotVal": 1, 
        "desc": "很好看", 
        "author": {
            "name": "", 
            "tags": [ ]
        }, 
        "wordCount": 24253, 
        "lastUpdateChapter": {
            "id": 0, 
            "name": "string", 
            "time": "2020-03-30T09:00:51.066Z"
        }, 
        "lastUpdateTime": "2020-03-30T09:00:51.066Z"
    }
}



2.书籍章节列表
pid:002002

param:

参数	数据类型	是否必填	说明
bookId	string	是	书籍id


{
    "retCd": 0, 
    "retMsg": "string", 
    "data": {
        "total": 0, 
        "volumes": [
            {
                "id": 1, 
                "name": "第一卷", 
                "seqId": "0", 
                "chapters": [
                    {
                        "id": 0, 
                        "volumeId": 1, 
                        "seqId": 0, 
                        "name": "string", 
                        "wordCount": 0, 
                        "updated": "2020-03-30T09:22:25.975Z"
                    }
                ]
            }
        ]
    }
}


3.书籍章节内容
pid:002003

param:

参数	数据类型	是否必填	说明
bookId	string	是	书籍id
chapterId	string	是	章节id


{
    "retCd": 0,  
    "retMsg": "string", 
    "data": {
        "bookId": 0, 
        "chapterId": 0, 
        "chapterName": "string", 
        "content": "string", 
        "publishTime": "2017-04-28T10:10:10Z"
    }
}


4.书籍下载
接口地址：http://ab-dev.y5en.com/brs-app/download.sec(下载使用独立接口)

pid:002004

param:

参数	数据类型	是否必填	说明
bookId	string	是	书籍id


zip文件





三、分类接口
1.获取所有分类
pid:003001

{
    "retCd": 0,  
    "retMsg": "string", 
    "data": [
        {
            "id": 1, 
            "name": "男生", 
            "level": 0, 
            "cates": [
                {
                    "id": 2, 
                    "parentId": 1, 
                    "level": 1, 
                    "name": "都市", 
                    "cover": "http://xx"
                }, 
                {
                    "id": 2, 
                    "parentId": 1, 
                    "level": 1, 
                    "name": "玄幻", 
                    "cover": "http://xx"
                }
            ]
        }
    ]
}


2.按分类获取书籍列表
pid:003002

param:

参数	数据类型	是否必填	说明
cate	int	是	分类id
wordCount	int	否	字数筛选  0-100万字以下  1-100万到300万字 2-三百万以上
state	int	否	书籍状态，0-完结 1-连载中 3-今日更新
page	int	否	数据页数，默认1
limit	int	否	数据条数，默认8
sort	int	否	排序 0-热门 1-最新 2-评分


{
    "retCd": 0,  
    "retMsg": "string", 
    "data": [
        {
            "id": 0, 
            "name": "神医庶女", 
            "cover": "http://www.baidu.com", 
            "cates": [
                "玄幻"
            ], 
            "tags": [
                "标签"
            ], 
            "finishState": 1, 
            "score": "10", 
            "popVal": "2131", 
            "hotVal": "1231", 
            "fansVal": "1231", 
            "desc": "很好看"
        }
    ]
}
3.分类猜你喜欢
pid:003003

{
  "retCd": 0,
  "retMsg": "string",
  "data": [
    {
      "id": 2,
      "parentId": 1,
      "level": 1,
      "name": "都市"
    },
    {
      "id": 2,
      "parentId": 1,
      "level": 1,
      "name": "玄幻"
    }
  ]
}


四、搜索接口
1.搜索发现
pid:004001

{
    "retCd": 0,  
    "retMsg": "string", 
    "data": [
        {
            "word": "string"
        }
    ]
}


2.搜索推荐
pid:004002

param:

参数	数据类型	是否必填	说明
word	string	是	输入的关键词


{
    "retCd": 0,  
    "retMsg": "string",  
    "data": [
        {
            "word": "string"
        }
    ]
}


3.书籍搜索
pid:003003

param:

参数	数据类型	是否必填	说明
q	string	是	搜索关键字，标题或作者
limit	int	否	数据条数，默认3


{
    "retCd": 0,  
    "retMsg": "string", 
    "data": [
        {
            "id": 0, 
            "name": "神医庶女", 
            "cover": "http://www.baidu.com", 
            "cates": [
               "玄幻"
            ], 
            "tags": [
                "标签"
            ], 
            "finishState": 1, 
            "score": "10", 
            "popVal": "2131", 
            "hotVal": "1231", 
            "fansVal": "1231", 
            "desc": "很好看"
        }
    ]
}






