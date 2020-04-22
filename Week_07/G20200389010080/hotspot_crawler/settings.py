# -*- coding: utf-8 -*-

# Scrapy settings for hotspot_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import datetime

BOT_NAME = 'hotspot_crawler'

SPIDER_MODULES = ['hotspot_crawler.spiders.TencentHotspot', 'hotspot_crawler.spiders.SohuHotspot',
                  'hotspot_crawler.spiders.XinhuaHotspot', 'hotspot_crawler.spiders.HuanqiuHotspot',
                  'hotspot_crawler.spiders.BaiduHotspot', 'hotspot_crawler.spiders.FengHuangHotspot',
                  'hotspot_crawler.spiders.SinaHotspot', 'hotspot_crawler.spiders.doubanComment']
NEWSPIDER_MODULE = 'hotspot_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'hotspot_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'hotspot_crawler.middlewares.HotspotCrawlerSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'hotspot_crawler.middlewares.HotspotCrawlerDownloaderMiddleware': 543,
    'hotspot_crawler.middlewares.UserAgentMiddleware': 616,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'hotspot_crawler.pipelines.JSONWithEncodingPipeline': 300,
    'hotspot_crawler.pipelines.BlogscrapyPipeline': 400,
    # 'hotspot_crawler.pipelines.ImageGettingPipeline': 300, 日后扩展图片下载功能备用
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
today = datetime.datetime.now()
LOG_FILE = "../log/{}.log".format(today.strftime('%Y%m%d_%H%M%S'))
HTTPERROR_ALLOWED_CODES = [400, ]
FEED_EXPORT_ENCODING = 'utf-8'


# ######## settings.py ##########
# #mysql-config
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'root'
MYSQL_PASSWD ='rootroot'
MYSQL_PORT = 3306

# ######## 表结构 ##########
# CREATE TABLE `news` (
#   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
#   `title` varchar(200) DEFAULT NULL COMMENT '新闻标题',
#   `source` varchar(200) DEFAULT NULL COMMENT '新闻来源',
#   `source_from` varchar(200) DEFAULT NULL COMMENT '新闻二级来源',
#   `publish_time` varchar(200) DEFAULT NULL COMMENT '发布日期',
#   `newsId` varchar(200) DEFAULT NULL COMMENT '新闻ID',
#   `keywords` varchar(200) DEFAULT NULL COMMENT '新闻关键词',
#   `content_url` varchar(200) DEFAULT NULL COMMENT '新闻链接',
#   `media_url` varchar(200) DEFAULT NULL COMMENT '新闻图片',
#   `content` text DEFAULT NULL COMMENT '新闻内容',
#   `comment_list` text DEFAULT NULL COMMENT '新闻评论',
#   `abstract` text DEFAULT NULL COMMENT '新闻摘要',
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8mb4

