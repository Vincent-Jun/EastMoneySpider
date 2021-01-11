# -*- coding: utf-8 -*-
import scrapy
from EastMoneySpider.common.MySqlDatabase import MySqlHelper
from EastMoneySpider.items import SinaRealItem
from EastMoneySpider.common.ParseConfig import getDbConfig
from EastMoneySpider.common.WriteLog import MyLogger

class SinarealSpider(scrapy.Spider):
    name = 'SinaReal'
    allowed_domains = ['sinajs.cn']
    logger = MyLogger("SinarealSpider")

    def start_requests(self):
        dbConfig = getDbConfig()
        mysqlDataHelp = MySqlHelper(dbConfig[0], dbConfig[1], dbConfig[2], dbConfig[3])
        itemList = mysqlDataHelp.get("SELECT `证券代码` FROM companyinfo WHERE `上市状态` != '暂停上市'")
        count = 1
        param = ""
        for item in itemList:
            code = item[0]
            if int(code) >= 600000:
                code = "sh" + code
            else:
                code = "sz" + code

            if count > 1:
                param += ","

            count += 1
            param += code
            if count > 51 or itemList[-1] == item:
                url = "http://hq.sinajs.cn/list=%s" % param
                count = 1
                param = ""
                yield scrapy.Request(url=url, callback=self.parse)


#股票名称、今日开盘价、昨日收盘价、当前价格、今日最高价、今日最低价、竞买价、竞卖价、成交股数、成交金额、买1手、买1报价、买2手、买2报价、…、买5报价、…、卖5报价、日期、时间
    def parse(self, response):
        result = response.text.split(";")
        sinaRealItem = SinaRealItem()
        try:
            for item in result:
                data = item.split("=")
                if len(data) == 2:
                    temp = data[0]
                    sinaRealItem["s1"] = temp[-6 :]
                    temp = data[1].replace('"',"")
                    priceData = temp.split(",")
                    index = 2
                    temp = len(priceData)
                    for itemData in priceData:
                        sinaRealItem["s%d" % index] = itemData
                        index = index + 1
                    yield sinaRealItem
        except Exception as e:
            self.logger.error("Request Url = %s, Error Info: %s" % (response.url, e))
