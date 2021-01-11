# -*- coding: utf-8 -*-
import scrapy
import time
import json
from EastMoneySpider.items import EastMoneyLHBItem
from EastMoneySpider.common.WriteLog import MyLogger

class EastmoneylhbSpider(scrapy.Spider):
    name = 'EastMoneyLHB'
    allowed_domains = ['data.eastmoney.com']
    start_urls = ['https://data.eastmoney.com']
    logger = MyLogger("EastmoneylhbSpider")

    def start_requests(self):
        url = "https://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=200,page=1,sortRule=-1,sortType=," \
              "startDate=%s,endDate=%s,gpfw=0,js=var%%20data_tab_1.html?rt=%d" \
              % (time.strftime("%Y-%m-%d", time.localtime()),
                 time.strftime("%Y-%m-%d", time.localtime()), int(time.time() / 60))
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.text
        temp = data.split("=", 1)
        #try:
        jsonData = temp[1]
        obj = json.loads(jsonData)
        parseItem = EastMoneyLHBItem()
        try:
            for item in obj['data']:
                parseItem["SCode"]= item["SCode"]
                parseItem["SName"]= item["SName"]
                parseItem["ClosePrice"]= item["ClosePrice"]
                parseItem["Chgradio"]= item["Chgradio"]
                parseItem["Dchratio"]= item["Dchratio"]
                parseItem["JmMoney"]= item["JmMoney"]
                parseItem["Turnover"]= item["Turnover"]
                parseItem["Ntransac"]= item["Ntransac"]
                parseItem["Ctypedes"]= item["Ctypedes"]
                parseItem["Smoney"]= item["Smoney"]
                parseItem["Bmoney"]= item["Bmoney"]
                parseItem["Tdate"]= item["Tdate"]
                parseItem["JmRate"]= item["JmRate"]
                parseItem["Ltsz"]= item["Ltsz"]
                parseItem["JD"]= item["JD"]
                yield parseItem
        except Exception as e:
            self.logger.error("Request Url = %s, Error Info: %s" % (response.url, e))