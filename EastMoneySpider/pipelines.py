# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from EastMoneySpider.items import ConvertibleBondItem
from EastMoneySpider.items import SinaRealItem
from EastMoneySpider.items import EastMoneyBKItem
from EastMoneySpider.items import EastMoneyCompanyInfoItem
from EastMoneySpider.items import EastMoneyBKGPItem
from EastMoneySpider.items import EastMoneyLHBItem

from EastMoneySpider.common.MySqlDatabase import MySqlHelper
from EastMoneySpider.common.ParseConfig import getDbConfig
import time

class EastmoneyspiderPipeline(object):
    def __init__(self):
        dbConfig = getDbConfig()
        self.mysqlDataHelp = MySqlHelper(dbConfig[0], dbConfig[1], dbConfig[2], dbConfig[3])

    def process_item(self, item, spider):
        if isinstance(item, ConvertibleBondItem):
            sql = "REPLACE INTO convertiblebond VALUES('%s','%s', %f, %f, '%s', '%s', %f, %f, %f, %f, %f, %f, " \
                  "%f, %f, %f, %f, '%s', '%s', '%s')" % (item['f12'], item['f14'], item['f2'], item['f3'], item['f232']
                                                   , item['f234'], item['f229'], item['f230'], item['f235'], item['f236']
                                                   , item['f237'], item['f238'], item['f239'], item['f240'], item['f241']
                                                  , item['f227'], item['f242'], item['f26'], item['f243'])
            self.mysqlDataHelp.execute(sql)

        if isinstance(item, SinaRealItem):
            sql = "REPLACE INTO sinareal VALUES('%s','%s','%s',%f,%f,%f,%f,%f,%f,%f," \
                  "%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)" \
                  %(item['s32'] + " " + item['s33'], item['s1'], item['s2'], float(item['s5'])/ float(item['s4'])*100 -100, float(item['s3']),
                  float(item['s4']), float(item['s5']), float(item['s6']), float(item['s7']), float(item['s8']), float(item['s9']),
                  float(item['s10']), float(item['s11']), float(item['s12']), float(item['s13']), float(item['s14']), float(item['s15']),
                  float(item['s16']), float(item['s17']), float(item['s18']), float(item['s19']), float(item['s20']), float(item['s21']),
                  float(item['s22']), float(item['s23']), float(item['s24']), float(item['s25']), float(item['s26']), float(item['s27']),
                  float(item['s28']), float(item['s29']), float(item['s30']), float(item['s31']))
            self.mysqlDataHelp.execute(sql)

        if isinstance(item, EastMoneyBKItem):
            sql = "REPLACE INTO bk VALUES('%s','%s','%s', %f, %f, %f, %f, %f, %f, %f, %f, " \
                  "%f, %f, %f, %f, '%s')" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),item['f12'], item['f14']
                  , float(item['f2']), float(item['f3']), float(item['f62'])
                  , float(item['f184']), float(item['f66']), float(item['f69']), float(item['f72']), float(item['f75'])
                  , float(item['f78']), float(item['f81']), float(item['f84']), float(item['f124'])
                  , item['f204'])
            self.mysqlDataHelp.execute(sql)

        if isinstance(item, EastMoneyCompanyInfoItem):
            sql = "REPLACE INTO companyinfo VALUES('%s','%s',%f, %f,'%s','%s','%s','%s','%s','%s')" \
                  %(item['s1'], item['s2'], int(item['s3']),int(item['s4']), item['s5'], item['s6']
                    , item['s7'], item['s8'], item['s9'], item['s10'])
            self.mysqlDataHelp.execute(sql)

        if isinstance(item, EastMoneyBKGPItem):
            sql = "REPLACE INTO bkgp VALUES('%s','%s', '%s')" % (item['bk'], item['f12'],item['f14'])
            self.mysqlDataHelp.execute(sql)

        if isinstance(item, EastMoneyLHBItem):
            sql = "REPLACE INTO lhb VALUES('%s','%s','%s',%f,%f,%f,%f,%f,%f,'%s',%f,%f,%f,%f,'%s')" %(item['Tdate'],
            item['SCode'],item['SName'],self.tofloat(item['ClosePrice']),self.tofloat(item['Chgradio']),self.tofloat(item['Dchratio']),
            self.tofloat(item['JmMoney']),self.tofloat(item['Turnover']),self.tofloat(item['Ntransac']),item['Ctypedes'],
            self.tofloat(item['Smoney']),self.tofloat(item['Bmoney']),self.tofloat(item['JmRate']),self.tofloat(item['Ltsz']),item['JD'])
            sql = sql.replace("%", "%%")
            self.mysqlDataHelp.execute(sql)


    def parseData(self, str):
        str = str.replace(' ','')
        if str.find('%') > 0:
            return float(str.replace('%', ''))
        if str.find('万') > 0:
            return float(str.replace('万','')) * 10000.0
        if str.find('亿') > 0:
            return float(str.replace('亿', '')) * 10000.0 * 10000.0
        return float(str)

    def tofloat(self, str):
        data = 0.0
        try:
            data = float(str)
        except:
            data = 0.0
        return data