所有接口使用相同的入口，依据pid区分 

接口地址：/brs.sec

登录部分参考连尚开放平台统一登





一、用户登录
用户登录

pid:101001

param:

参数	数据类型	是否必填	说明
code	string	是	授权码


{
  "retCd": 0,
  "retMsg": null,
  "data": {
    "unionId": "用户唯一id",
    "nickName": "用户昵称",
    "minHeadImg": "小头像",
    "headImg": "原头像",
    "accessToken": "访问令牌",
    "readSex": 0,
    "birthday": "1990-01-01",
    "bio": "居之无倦，行之以忠"
  }
}


用户登出

pid:101002

param:

参数	数据类型	是否必填	说明


{
  "retCd": 0,
  "retMsg": null
}


修改用户信息

pid:101003

param:

参数	数据类型	是否必填	说明
sex	int	否	真实性别 1男2女
readSex	int	否	性别偏好 1男2女
headImg	string	否	原头像修改后小头像自动修改
birthday	string	否	生日  1990-01-01
bio	string	否	个性签名


{
  "retCd": 0,
  "retMsg": null,
  "data": {
    "unionId": "用户唯一id",
    "nickName": "用户昵称",
    "minHeadImg": "小头像",
    "headImg": "原头像",
    "accessToken": "访问令牌",
    "readSex": 0,
    "birthday": "1990-01-01",
    "bio": "居之无倦，行之以忠"
  }
}


加入用户书架

pid:101004 返回加入后书架

param:

参数	数据类型	是否必填	说明
bookId	string	是	书籍id  int,int,int...


{
  "retCd": 0,
  "retMsg": null,
  "data": [
    {
      "id": 100001,
      "name": "书名",
      "cover": "封面",
      "totalChapterNum": 100,
      "readChapterNum": 7,
      "chapterId": "阅读章节id",
      "chapterName": "阅读章节标题"
    }
  ]
}


用户书架列表

pid:101005

param:

参数	数据类型	是否必填	说明


{
  "retCd": 0,
  "retMsg": null,
  "data": [
    {
      "id": 100001,
      "name": "书名",
      "cover": "封面",
      "state": "书籍状态",
      "totalChapterNum": 100,
      "readChapterNum": 7,
      "exclusive": 1, // 是否独家内容
      "chapterId": "阅读章节id",
      "chapterName": "阅读章节标题"
    }
  ]
}


阅读历史

pid:101006

param:

参数	数据类型	是否必填	说明
page	int	否	默认1
limit	init	否	默认30


{
  "retCd": 0,
  "retMsg": null,
  "data": [
    {
      "id": 100001,
      "name": "书名",
      "cover": "封面",
      "state": "书籍状态",
      "totalChapterNum": 100,
      "readChapterNum": 7,
      "exclusive": 1, // 是否独家内容
      "chapterId": "阅读章节id",
      "chapterName": "阅读章节标题"
    }
  ]
}


设备信息初始化

pid:101007

param:

参数	数据类型	是否必填	说明
readSex

string

否

性别偏好，男-M 女-F

originalChannelId

string

否

原始渠道id

imei

string

否


imsi

string

否


mac

string

否


idfv

string

否


osVerName

string

否

手机系统版本名称

osVerCode

string

否

手机系统版本号

scrH

int

否

设备屏幕分辨率高

scrW

int

否

设备屏幕分辨率宽

manufacturer

string

否

手机生产厂商

model

string

否

手机型号

pushToken

string

否




{
  "retCd": 0,
  "retMsg": null,
  "data": true
}




阅读进度上传

pid:101008

param:



参数	数据类型	子参数	子数据类型	是否必填	说明
readingProgress

string(json array序列化)	bookId	int	是	书籍


volumeId	int	是	卷id


chapterId	int	是	章节


seqId
int	是	章节seqId


chapterOffset	int	是	字数偏移量


percent	int	是	整本书的百分比


lastReadTime	long	是	最后阅读时间（unix时间戳）


{
  "retCd": 0,
  "retMsg": null,
  "data": null
}


移出用户书架 返回移出后书架

pid:101009

param:

参数	数据类型	是否必填	说明
bookId	int	是	书籍id


{
  "retCd": 0,
  "retMsg": null,
  "data": [
    {
      "id": 100001,
      "name": "书名",
      "cover": "封面",
      "state": "书籍状态",
      "totalChapterNum": 100,
      "readChapterNum": 7,
      "exclusive": 1, // 是否独家内容
      "chapterId": "阅读章节id",
      "chapterName": "阅读章节标题"
    }
  ]
}


阅读进度批量获取

pid:101010

param:

参数	数据类型	是否必填	说明
bookIds	string	是	书籍id，多个使用英文,隔开


{
  "retCd": 0,
  "retMsg": null,
  "data": [
    {
      "bookId": 100001,
      "volumeId": 1,
      "chapterId": 1,
      "seqId": 1,
      "chapterOffset": 1223,
      "percent": 62,
      "lastReadTime": 1232394252
    }
  ]
}


清空阅读历史

pid:101011



{
  "retCd": 0,
  "retMsg": null,
  "data": true
