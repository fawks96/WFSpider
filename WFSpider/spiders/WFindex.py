# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WFSpider.pipelines import MongoDBPipleline
from scrapy.http import Request
from scrapy.loader import ItemLoader
from WFSpider.items import JournalItem
logging.getLogger().setLevel(logging.INFO)
mongo_cli = MongoDBPipleline()

class WfindexSpider(CrawlSpider):
    name = 'WFindex'
    # allowed_domains = ['wanfangdata']
    # start_urls = ['http://c.g.wanfangdata.com.cn/Periodical.aspx']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Periodical.aspx'), callback='parse_item', follow=True),
    # )

    def start_requests(self):

        for _class in mongo_cli.mainindex.find({}):
            sub_list = _class.get('sub_class')
            for sub_class in sub_list:
                # yield Request("http://c.g.wanfangdata.com.cn/PeriodicalSubject.aspx?NodeId=C",
                #               callback=self.parse_item,
                #               meta={"_class": _class,
                #                     "sub_class": sub_class})
                yield Request(sub_class.get('url'),
                              callback=self.parse_item,
                              meta={"_class": _class,
                                    "sub_class": sub_class})


    def parse_item(self, response):
        base_url = 'http://c.g.wanfangdata.com.cn/%s'
        try:
            response.meta['_class'].pop('sub_class')
        except KeyError:
            pass
        for item in response.xpath('//*[@id="divperilist"]/ul/li'):
            l = ItemLoader(item=JournalItem(), selector=item)
            l.add_value('_class', response.meta['_class'])
            l.add_value('sub_class', response.meta['sub_class'])
            l.add_value('rss', base_url % item.xpath('a[1]/@href').extract()[0])
            l.add_xpath('name', 'a[2]/text()')
            l.add_value('url', base_url % item.xpath('a[2]/@href').extract()[0])
            yield l.load_item()
        next_page = u"下一页"
        find_next = response.xpath(u".//a[@href][t/text()='%s']" % next_page).xpath('@href')
        if find_next:
            next_url = base_url % find_next.extract()[0]
            yield Request(next_url, callback=self.parse_item, meta=response.meta)



