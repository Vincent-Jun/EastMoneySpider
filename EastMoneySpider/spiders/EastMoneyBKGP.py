# -*- coding: utf-8 -*-
import scrapy
import time
import json
from EastMoneySpider.common.MySqlDatabase import MySqlHelper
from EastMoneySpider.common.ParseConfig import getDbConfig
from EastMoneySpider.items import EastMoneyBKGPItem
from EastMoneySpider.common.WriteLog import MyLogger

class EastmoneybkgpSpider(scrapy.Spider):
    name = 'EastMoneyBKGP'
    allowed_domains = ['73.push2.eastmoney.com']
    start_urls = ['http://73.push2.eastmoney.com']
    bkCodeUrl = {}
    logger = MyLogger("EastmoneybkgpSpider")

    def start_requests(self):
        dbConfig = getDbConfig()
        mysqlDataHelp = MySqlHelper(dbConfig[0], dbConfig[1], dbConfig[2], dbConfig[3])
        sql = "SELECT bk.`板块代码` FROM bk"
        bkCodeList = mysqlDataHelp.get(sql)
        for bkCode in bkCodeList:
            for pn in range(1, 5):
                url = "http://push2.eastmoney.com/api/qt/clist/get?pn=%d&pz=50&po=1&np=1&fltt=2&invt=2&fid=f62&fs=b:%s&stat=1&fields=" \
                    "f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124&rt=%d" %(pn, bkCode[0], int(time.time() / 30))
                self.bkCodeUrl[url] = bkCode[0]
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.text
        obj = json.loads(data)
        parseItem = EastMoneyBKGPItem()
        parseItem['bk'] = self.bkCodeUrl[response.url]
        try:
            for item in obj['data']['diff']:
                parseItem['f12'] = item['f12']
                parseItem['f14'] = item['f14']
                yield parseItem
        except Exception as e:
            self.logger.error("Request Url = %s, Error Info: %s" % (response.url, e))