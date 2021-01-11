# -*- coding: utf-8 -*-
import scrapy
import time
from EastMoneySpider.items import ConvertibleBondItem
import json
import os
from EastMoneySpider.common.WriteLog import MyLogger

class ConvertiblebondSpider(scrapy.Spider):
    name = 'ConvertibleBond'
    allowed_domains = ['73.push2.eastmoney.com']
    hasNext = True
    logger = MyLogger("ConvertiblebondSpider")

    def start_requests(self):
        pn = 0
        while(self.hasNext and pn < 10):
            pn += 1
            url = "http://73.push2.eastmoney.com/api/qt/clist/get?&pn=%d&pz=50&po=1&np=1&ut" \
                  "=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f243&fs=b:MK0354&fields" \
                  "=f1,f152,f2,f3,f12,f13,f14,f227,f228,f229,f230,f231,f232,f233,f234,f235,f236,f237,f238,f239," \
                  "f240,f241,f242,f26,f243&_=%d" % (pn, int(time.time() * 1000))
            yield scrapy.Request(url = url, callback=self.parse)

    def is_number(self, s):
        try:
            float(s)
            return s
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return s
        except (TypeError, ValueError):
            pass

        return 0

    def parse(self, response):
        parseItem = ConvertibleBondItem()
        data = response.text
        obj = json.loads(data)
        if obj['data'] is None:
            self.hasNext = False
        try:
            for item in obj['data']['diff']:
                parseItem['f12'] = item['f12']
                parseItem['f14'] = item['f14']
                parseItem['f2'] = self.is_number(item['f2'])
                parseItem['f3'] = self.is_number(item['f3'])
                parseItem['f232'] = item['f232']
                parseItem['f234'] = item['f234']
                parseItem['f229'] = self.is_number(item['f229'])
                parseItem['f230'] = self.is_number(item['f230'])
                parseItem['f235'] = self.is_number(item['f235'])
                parseItem['f236'] = self.is_number(item['f236'])
                parseItem['f237'] = self.is_number(item['f237'])
                parseItem['f238'] = self.is_number(item['f238'])
                parseItem['f239'] = self.is_number(item['f239'])
                parseItem['f240'] = self.is_number(item['f240'])
                parseItem['f241'] = self.is_number(item['f241'])
                parseItem['f227'] = self.is_number(item['f227'])
                parseItem['f242'] = item['f242']
                parseItem['f26'] = item['f26']
                parseItem['f243'] = item['f243']
                yield parseItem
        except Exception as e:
            self.hasNext = False
            self.logger.error("Request Url = %s, Error Info: %s" %(response.url, e))
