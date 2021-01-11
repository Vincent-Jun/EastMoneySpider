# -*- coding: utf-8 -*-
import scrapy
import time
import json
from EastMoneySpider.items import EastMoneyBKItem
from EastMoneySpider.common.WriteLog import MyLogger

class EastmoneybkSpider(scrapy.Spider):
    name = 'EastMoneyBK'
    allowed_domains = ['73.push2.eastmoney.com']
    start_urls = ['http://73.push2.eastmoney.com']
    hasNext = True
    logger = MyLogger("EastmoneybkSpider")

    def start_requests(self):
        pn = 0 # 目前有61个
        while (self.hasNext):
            pn += 1
            url = "http://push2.eastmoney.com/api/qt/clist/get?pn=%d&pz=50&po=1&np=1" \
                  "&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f62&fs=m:90+t:2&stat=1" \
                  "&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124&rt=%d"\
                  % (pn, int(time.time() / 30))
            if pn == 2:
                self.hasNext = False
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.text
        obj = json.loads(data)
        parseItem = EastMoneyBKItem()
        if obj['data'] is None:
            self.hasNext = False
        try:
            for item in obj['data']['diff']:
                parseItem['f2'] = item['f2']
                parseItem['f3'] = item['f3']
                parseItem['f12'] = item['f12']
                parseItem['f14'] = item['f14']
                parseItem['f62'] = item['f62']
                parseItem['f66'] = item['f66']
                parseItem['f69'] = item['f69']
                parseItem['f72'] = item['f72']
                parseItem['f75'] = item['f75']
                parseItem['f78'] = item['f78']
                parseItem['f81'] = item['f81']
                parseItem['f84'] = item['f84']
                parseItem['f124'] = item['f124']
                parseItem['f184'] = item['f184']
                parseItem['f204'] = item['f204']
                parseItem['f205'] = item['f205']
                yield parseItem
        except Exception as e:
            self.hasNext = False
            self.logger.error("Request Url = %s, Error Info: %s" % (response.url, e))
