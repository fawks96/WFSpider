# -*- coding: utf-8 -*-
import pymongo
from WFSpider.items import *
import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
logging.getLogger().setLevel(logging.INFO)

class MongoDBPipleline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        db = client["WanFang"]
        self.mainindex = db["MainIndex"]
        self.journal = db["Journal"]
        self.article = db["Article"]
        self.others = db["Others"]

    def process_item(self, item, spider):
        if isinstance(item, SubjectItem):
            try:
                self.mainindex.insert(item)
            except Exception, e:
                logging.exception("")
        elif isinstance(item, JournalItem):
            try:
                find_res = self.journal.find_one(dict(item))
                if find_res:
                    logging.info("dupelicated: %s" % item)
                else:
                    self.journal.insert(item)
            except:
                logging.exception("")
        elif isinstance(item, ArticleItem):
            if item.get('title'):
                try:
                    for key in item:
                        item[key] = [x for x in item[key] if x]
                    find_res = self.article.find_one(dict(item))
                    if find_res:
                        logging.info("dupelicated: %s" % item)
                    else:
                        self.article.insert(item)
                except:
                    logging.exception("")
        return item
