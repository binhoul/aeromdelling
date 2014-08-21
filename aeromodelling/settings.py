# -*- coding: utf-8 -*-

# Scrapy settings for aeromodelling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'aeromodelling'

SPIDER_MODULES = ['aeromodelling.spiders']
NEWSPIDER_MODULE = 'aeromodelling.spiders'
DEFAULT_ITEM_CLASS = 'aeromodelling.items.AeromodellingItem'
ITEM_PIPELINES = ['aeromodelling.pipelines.MongoDBPipeline',]

#mongodb
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DATABASE = 'mx3g'
MONGODB_COLLECTION = 'mainpost'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aeromodelling (+http://www.yourdomain.com)'
#取消默认的useragent,使用新的useragent
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
#    'AeromodelSpider.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
# }
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'aeromodelling.rotate_useragent.RotateUserAgentMiddleware' :400
    }
