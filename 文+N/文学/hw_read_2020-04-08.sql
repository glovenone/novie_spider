# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 10.2.228.70 (MySQL 5.6.29-76.2-log)
# Database: hw_read
# Generation Time: 2020-04-08 09:56:25 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table authors
# ------------------------------------------------------------

DROP TABLE IF EXISTS `authors`;

CREATE TABLE `authors` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `provider_id` int(11) DEFAULT NULL,
  `provider_author_id` bigint(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='作者表';



# Dump of table book_categories
# ------------------------------------------------------------

DROP TABLE IF EXISTS `book_categories`;

CREATE TABLE `book_categories` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `cate_id` int(11) DEFAULT NULL,
  `is_primary` tinyint(1) DEFAULT '0',
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table book_marks
# ------------------------------------------------------------

DROP TABLE IF EXISTS `book_marks`;

CREATE TABLE `book_marks` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT '0',
  `book_id` int(11) DEFAULT '0',
  `volume_id` int(11) DEFAULT '0',
  `chapter_id` int(11) DEFAULT '0',
  `chapter_name` varchar(200) DEFAULT NULL,
  `chapter_offset` int(11) DEFAULT '0' COMMENT '章内字的偏移位置',
  `short_chapter` varchar(50) DEFAULT NULL COMMENT 'offset处文章简短内容',
  `client_addmark_dt` datetime DEFAULT NULL COMMENT '客户端加书签时间',
  `device_id` bigint(20) DEFAULT '0',
  `platform` varchar(12) DEFAULT NULL,
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='书签';



# Dump of table book_ranking_list
# ------------------------------------------------------------

DROP TABLE IF EXISTS `book_ranking_list`;

CREATE TABLE `book_ranking_list` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `rank_type` int(11) NOT NULL DEFAULT '0' COMMENT '榜单类型',
  `book_id` int(11) DEFAULT NULL,
  `book_name` varchar(128) DEFAULT NULL,
  `book_cover` varchar(128) DEFAULT NULL,
  `cates` varchar(128) DEFAULT NULL,
  `tags` varchar(128) DEFAULT NULL,
  `finish` tinyint(1) DEFAULT '0' COMMENT '当前状态：0=连载中，1=已完本',
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `score` varchar(64) DEFAULT NULL,
  `popVal` varchar(64) DEFAULT NULL,
  `hotVal` varchar(64) DEFAULT NULL,
  `fansVal` varchar(64) DEFAULT NULL,
  `desc` varchar(128) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table book_tags
# ------------------------------------------------------------

DROP TABLE IF EXISTS `book_tags`;

CREATE TABLE `book_tags` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  `type` tinyint(1) DEFAULT NULL COMMENT '0=systag,1=author tag,2=editor tag',
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `type` (`type`,`status`),
  KEY `tag_book` (`book_id`,`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table books
# ------------------------------------------------------------

DROP TABLE IF EXISTS `books`;

CREATE TABLE `books` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0:小说 1:漫画 2:杂志 3出版 4短篇小说',
  `read_type` tinyint(1) DEFAULT '0' COMMENT '0全支持1上下',
  `provider_id` int(11) DEFAULT NULL COMMENT '来源ID',
  `provider_book_id` bigint(20) DEFAULT NULL,
  `provider_channel_id` int(11) DEFAULT '0',
  `provider_cate1_id` bigint(20) DEFAULT '0',
  `provider_cate2_id` bigint(20) DEFAULT '0',
  `provider_cate3_id` bigint(20) DEFAULT '0',
  `name` varchar(200) DEFAULT NULL,
  `cover` varchar(200) DEFAULT NULL,
  `cover_new` varchar(200) DEFAULT NULL COMMENT '本站书籍封面地址',
  `author_id` int(11) DEFAULT NULL,
  `cate1_id` int(11) DEFAULT '0' COMMENT '这个是我们自己的分类id',
  `cate2_id` int(11) DEFAULT '0',
  `cate3_id` int(11) DEFAULT '0',
  `extend_cates` tinyint(1) DEFAULT '0' COMMENT '是否有扩展分类',
  `intro` varchar(200) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `word_count` bigint(11) DEFAULT '0',
  `volume_count` int(11) DEFAULT '0',
  `chapter_count` int(11) DEFAULT '0',
  `favorite_count` bigint(20) DEFAULT '0',
  `click_count` bigint(20) DEFAULT '0' COMMENT '总点击数',
  `week_click_count` bigint(20) DEFAULT '0' COMMENT '周点击数',
  `month_click_count` bigint(20) DEFAULT '0' COMMENT '月点击数',
  `recommend_count` bigint(20) DEFAULT '0' COMMENT '推荐数',
  `comment_count` bigint(20) DEFAULT '0' COMMENT '评论数',
  `discuss_count` bigint(20) DEFAULT '0' COMMENT '书籍讨论区总评论数（书评区）',
  `read_count` bigint(20) DEFAULT '0',
  `buy_count` int(11) DEFAULT '0',
  `rank` float DEFAULT NULL,
  `vip` tinyint(1) DEFAULT '0',
  `price` int(11) DEFAULT '0',
  `modified` tinyint(1) DEFAULT '0' COMMENT '是否被后台编辑过',
  `finish` tinyint(1) DEFAULT '0' COMMENT '当前状态：0=连载中，1=已完本',
  `finish_time` datetime DEFAULT NULL COMMENT '完本时间',
  `last_update_chapter` varchar(1000) DEFAULT NULL,
  `last_update_time` datetime DEFAULT NULL,
  `state` tinyint(1) DEFAULT '0' COMMENT '-100=未上架 0=能购买，1=能看不能买，2=下架，3=强制下架',
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0' COMMENT '0=正常 -1=删除的 -100=未上架 2=下架 3=强制下架',
  `add_shelf_time` datetime DEFAULT NULL COMMENT '上架时间',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL COMMENT 'spider test only',
  `sync_time` datetime DEFAULT NULL,
  `buy_state` tinyint(4) DEFAULT '0' COMMENT '0:默认值 1:全本购买，2:全本购买可试读',
  `mark` int(11) DEFAULT '0',
  `in_app` tinyint(4) DEFAULT '0' COMMENT '0:默认,1:在免费版中显示,后续加app使用二进制模式显示',
  `vip_category` tinyint(4) DEFAULT '0' COMMENT '0:默认 2:广告书籍 1:vip包月书籍',
  `hide` tinyint(4) DEFAULT '0' COMMENT '书籍是否隐藏1隐藏，0不隐藏',
  `book_hide` tinyint(4) DEFAULT '0' COMMENT '书籍是否隐藏1隐藏，0不隐藏',
  `book_level` tinyint(4) DEFAULT '0' COMMENT '书籍评级',
  PRIMARY KEY (`id`),
  UNIQUE KEY `provider_id` (`provider_id`,`provider_book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='书籍表';



# Dump of table categories
# ------------------------------------------------------------

DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `channel_id` int(11) DEFAULT '0' COMMENT '1:男频 2：女频',
  `level` int(11) DEFAULT NULL COMMENT '分类层级1-3',
  `parent_id` int(11) DEFAULT '0',
  `cate1_id` int(11) DEFAULT '0',
  `cate2_id` int(11) DEFAULT '0',
  `cate3_id` int(11) DEFAULT '0',
  `name` varchar(50) DEFAULT NULL,
  `cover` varchar(200) DEFAULT '',
  `cate_cover` varchar(200) DEFAULT NULL COMMENT '分类背景封面',
  `intro` varchar(100) DEFAULT NULL,
  `book_count` int(11) DEFAULT '0',
  `seq_id` int(11) DEFAULT NULL COMMENT '排序',
  `hidden` tinyint(1) DEFAULT NULL COMMENT '是否隐藏分类',
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='书籍分类';



# Dump of table chapter_contents
# ------------------------------------------------------------

DROP TABLE IF EXISTS `chapter_contents`;

CREATE TABLE `chapter_contents` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `volume_id` int(11) DEFAULT '0',
  `chapter_id` int(11) DEFAULT NULL,
  `encoding` varchar(32) DEFAULT NULL,
  `content` mediumtext,
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `sync_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chapter_id` (`chapter_id`),
  KEY `book_id` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='章节内容';



# Dump of table chapters
# ------------------------------------------------------------

DROP TABLE IF EXISTS `chapters`;

CREATE TABLE `chapters` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `provider_id` int(11) DEFAULT '0',
  `book_id` int(11) DEFAULT '0',
  `provider_book_id` bigint(20) DEFAULT '0',
  `volume_id` int(11) DEFAULT '0',
  `provider_volume_id` bigint(20) DEFAULT '0',
  `provider_chapter_id` bigint(20) DEFAULT NULL,
  `seq_id` int(11) DEFAULT '0',
  `name` varchar(200) DEFAULT NULL,
  `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
  `word_count` bigint(20) DEFAULT '0',
  `read_count` bigint(20) DEFAULT '0',
  `charset` varchar(32) DEFAULT NULL COMMENT '章节内容的字符集',
  `price` int(11) DEFAULT '0' COMMENT '总价',
  `unit_price` int(11) DEFAULT '0' COMMENT '单价',
  `vip` tinyint(1) DEFAULT '0',
  `last_update_time` int(11) DEFAULT NULL,
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL COMMENT 'spider test only',
  `sync_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `url` (`url`),
  KEY `vol_id` (`volume_id`),
  KEY `book_pc` (`provider_id`,`provider_chapter_id`,`book_id`),
  KEY `book_id` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='章节表，没有内容的';



# Dump of table risk_words
# ------------------------------------------------------------

DROP TABLE IF EXISTS `risk_words`;

CREATE TABLE `risk_words` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL DEFAULT '',
  `source` varchar(50) NOT NULL DEFAULT '',
  `level` varchar(50) NOT NULL DEFAULT '',
  `word` varchar(255) NOT NULL DEFAULT '',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0有效，1无效',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word` (`word`),
  KEY `created` (`created`),
  KEY `updated` (`updated`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='敏感关键字';



# Dump of table search_keyword
# ------------------------------------------------------------

DROP TABLE IF EXISTS `search_keyword`;

CREATE TABLE `search_keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(100) NOT NULL,
  `search_times` int(11) DEFAULT '0' COMMENT '检索次数',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='热门搜索关键字';



# Dump of table tags
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tags`;

CREATE TABLE `tags` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table volumes
# ------------------------------------------------------------

DROP TABLE IF EXISTS `volumes`;

CREATE TABLE `volumes` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT '0',
  `provider_id` int(11) DEFAULT '0',
  `provider_book_id` bigint(20) DEFAULT '0',
  `provider_volume_id` bigint(20) DEFAULT '0',
  `seq_id` int(11) DEFAULT '0',
  `name` varchar(200) DEFAULT NULL,
  `word_count` bigint(20) DEFAULT '0',
  `chapter_count` int(11) DEFAULT '0',
  `vip` tinyint(1) DEFAULT '0',
  `version` int(11) DEFAULT '0',
  `status` tinyint(1) DEFAULT '0',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `sync_time` datetime DEFAULT NULL,
  `parent_id` int(11) NOT NULL DEFAULT '-1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='书籍分卷，是否有卷按照books.have_volume判定';




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
