# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from aeromodelling.items import AeromodellingItem



class AeromodelSpider(CrawlSpider):
    name = "aeromodel"
    allowed_domains = ["mx3g.com"]
    download_delay = 0.25
    start_urls = (
        'http://bbs.mx3g.com/',
#        'http://bbs.mx3g.com/forum-8-1.html',
    )
    rules = ( 
            Rule(LinkExtractor(allow=('/forum-\d+-1\.html'),allow_domains=('mx3g.com'), restrict_xpaths=('//td[@class="fl_g"]/dl/dt/a')), callback='page_parse'),
#           Rule(LinkExtractor(allow=('/thread-\d+-1-1\.html'), allow_domains=('mx3g.com')), callback='art_parse'),
#           Rule(LinkExtractor(allow=('/forum-\d+-\d+\.html'), allow_domains=('mx3g.com'), restrict_xpaths=('//div[@id="pgt"]/div/a[@class="nxt"]')), callback='page_parse',follow=True),
            )

    def page_parse(self, response):
        sel = Selector(response)
        pageUrls = sel.xpath('//tbody[starts-with(@id,"normalthread_")]/tr/td[@class="icn"]/a/@href').extract()
        
        for pageUrl in pageUrls:
            yield scrapy.Request(pageUrl, callback=self.art_parse)


    def art_parse(self, response):
        sel = Selector(response)
        item = AeromodellingItem()
        item['postUrl'] = response.url
        item['postId'] = re.search(r'thread-(\d+)-', item['postUrl']).group(1)
        item['postAuthor'] = response.xpath('//div[@class="pi"]/div[@class="authi"]/a/text()')[0].extract()
        item['postTitle'] = response.xpath('//h1[@class="ts"]/a/text()').extract()
        item['postDate'] = response.xpath('//div[@class="authi"]/em[starts-with(@id,"authorposton")]')[0].re('\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}')
        item['repostCount'] = response.xpath('//div[@class="hm"]/span[@class="xi1"]/text()')[1].extract()
        postlist = response.xpath('//div[@id="postlist"]/div[starts-with(@id, "post_")]/@id').extract()
        xpathrule = '//div[starts-with(@id, "%s")]/descendant::td[starts-with(@id, "postmessage_")]/text()' %(postlist[0])
#item['postText'] = response.xpath(xpathrule).extract()
        return item
