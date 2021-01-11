# -*- coding: utf-8 -*-
import scrapy
from EastMoneySpider.items import EastMoneyCompanyInfoItem
import json
from EastMoneySpider.common.WriteLog import MyLogger

class EastmoneycompanyinfoSpider(scrapy.Spider):
    name = 'EastMoneyCompanyInfo'
    allowed_domains = ['data.eastmoney.com']
    start_urls = ['http://data.com/']
    hasNext = True
    logger = MyLogger("EastmoneycompanyinfoSpider")

    def start_requests(self):
        pn = 0
        while (self.hasNext):
            pn += 1
            url = "http://data.eastmoney.com/dataapi/gstc/search?st=ChangePercent&sr=-1&ps=20&p=%d&mainPoint=Qbtc" % pn
            yield scrapy.Request(url=url, callback=self.parse)

    def modifyString(self, data):
        data = data.replace("%","%%")
        data = data.replace('"','”')
        data = data.replace("'","‘")
        return data

    def parse(self, response):
        data = response.text
        obj = json.loads(data)
        parseItem = EastMoneyCompanyInfoItem()
        if obj['Data'] is None:
            self.hasNext = False
        try:
            for item in obj['Data']:
                parseItem['s1'] = item['SECURITYCODE']
                parseItem['s2'] = item['SECURITYSHORTNAME']
                parseItem['s3'] = item['ZGB']
                parseItem['s4'] = item['LTGB']
                parseItem['s5'] = item['LISTINGDATE']
                parseItem['s6'] = self.modifyString(item['COMPPROFILE'])
                parseItem['s7'] = item['BK']
                parseItem['s8'] = self.modifyString(item['MAINBUSIN'])
                parseItem['s9'] = self.modifyString(item['ZYCP'])
                parseItem["s10"] = item['LISTINGTYPE']
                yield parseItem
        except Exsception as e:
            elf.hasNext = False
            self.logger.error("Request Url = %s, Error Info: %s" % (response.url, e))