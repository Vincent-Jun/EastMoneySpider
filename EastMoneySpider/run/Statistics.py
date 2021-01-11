# -*- coding: utf-8 -*-
import time
from EastMoneySpider.common.ParseConfig import getDbConfig
from EastMoneySpider.common.MySqlDatabase import MySqlHelper
from EastMoneySpider.common.WriteLog import MyLogger

class StatisticsHelper(object):
    mysqlDataHelp = None
    ltgbList = {}
    def __init__(self, logger):
        dbConfig = getDbConfig()
        self.mysqlDataHelp = MySqlHelper(dbConfig[0], dbConfig[1], dbConfig[2], dbConfig[3])
        self.logger = logger

    def delHistoryData(self, tableName, backDay = 7):
        t = time.localtime(time.time() - 24 * 60 * 60 * backDay)
        sql = "DELETE FROM `%s` WHERE `日期` < '%s'" % (tableName, time.strftime("%Y-%m-%d", t))
        self.mysqlDataHelp.execute(sql)

    def buildLtgbDic(self):
        sql = "SELECT `证券代码`, `流通股本` FROM companyinfo"
        data = self.mysqlDataHelp.get(sql)
        for item in data:
            try:
                self.ltgbList[item[0]] = item[1]
            except Exception as e:
                self.logger.error(e)

    def getLtgb(self, code):
        data = 0
        try:
            data = self.ltgbList[code]
        except :
            self.logger.error("%s LTGB is Null" % code)
        return data

    def dayData(self):
        self.buildLtgbDic()
        dateTime = time.strftime("%Y-%m-%d", time.localtime())
        sql = "SELECT `日期`,`证券代码`,`公司名`,`涨幅`,`开盘价`,`昨收价`,`当前价`,`最高价`,`最低价`,`成交量`,`成交额` FROM sinareal " \
              "WHERE `日期` > '%s 14:55:00' AND `日期` < '%s 15:35:00' ORDER BY `日期` ASC" %\
              (dateTime, dateTime)
        data = self.mysqlDataHelp.get(sql)
        for item in data:
            ltgb = self.getLtgb(item[1])
            rateChange = 0
            if ltgb > 1:
                rateChange = item[-2] / ltgb * 100
            sql = "REPLACE INTO day VALUES('%s', '%s', '%s', %f, %f, %f, %f, %f, %f, %f, %f, %f)" % \
                  (dateTime,item[1], item[2], item[3], item[4], item[5], item[6],
                   item[7], item[8], item[9], item[10], rateChange)
            self.mysqlDataHelp.execute(sql)

    def bkDayData(self):
        dateTime = time.strftime("%Y-%m-%d", time.localtime())
        sql = "SELECT * FROM bk WHERE `日期` > '%s 15:55:00' ORDER BY `日期` ASC" % (dateTime)
        data = self.mysqlDataHelp.get(sql)
        for item in data:
            sql = "REPLACE INTO bkday VALUES('%s','%s','%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, " \
                  "%f, %f, %f, %f, '%s')" % \
                  (dateTime, item[1], item[2], item[3], item[4], abs(item[5] / item[6] * 100), item[5], item[6],
                   item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15])
            self.mysqlDataHelp.execute(sql)


if __name__ == '__main__':
    test = StatisticsHelper()
    test.bkDayData()