# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SinaRealItem(scrapy.Item):
    s1 = scrapy.Field()
    s2 = scrapy.Field()
    s3 = scrapy.Field()
    s4 = scrapy.Field()
    s5 = scrapy.Field()
    s6 = scrapy.Field()
    s7 = scrapy.Field()
    s8 = scrapy.Field()
    s9 = scrapy.Field()
    s10 = scrapy.Field()
    s11 = scrapy.Field()
    s12 = scrapy.Field()
    s13 = scrapy.Field()
    s14 = scrapy.Field()
    s15 = scrapy.Field()
    s16 = scrapy.Field()
    s17 = scrapy.Field()
    s18 = scrapy.Field()
    s19 = scrapy.Field()
    s20 = scrapy.Field()
    s21 = scrapy.Field()
    s22 = scrapy.Field()
    s23 = scrapy.Field()
    s24 = scrapy.Field()
    s25 = scrapy.Field()
    s26 = scrapy.Field()
    s27 = scrapy.Field()
    s28 = scrapy.Field()
    s29 = scrapy.Field()
    s30 = scrapy.Field()
    s31 = scrapy.Field()
    s32 = scrapy.Field()
    s33 = scrapy.Field()
    s34 = scrapy.Field()
    s35 = scrapy.Field()

class ConvertibleBondItem(scrapy.Item):
    f12 = scrapy.Field() #转债代码
    f14 = scrapy.Field() #转债名称
    f2 = scrapy.Field() #转债最新价
    f3 = scrapy.Field() #转债涨跌幅
    f232 = scrapy.Field() #正股代码
    f234 = scrapy.Field() #正股名称
    f229 = scrapy.Field() #最新价
    f230 = scrapy.Field() #涨跌幅
    f235 = scrapy.Field() #转股价
    f236 = scrapy.Field() #转股价值
    f237 = scrapy.Field() #转股溢价率
    f238 = scrapy.Field() #纯债溢价率
    f239 = scrapy.Field() #回售触发价
    f240 = scrapy.Field() #强赎触发价
    f241 = scrapy.Field() #到期赎回价
    f227 = scrapy.Field() #纯债价值
    f242 = scrapy.Field() #开始转股日
    f26= scrapy.Field() #上市日期
    f243 = scrapy.Field() #申购日期

class EastMoneyBKItem(scrapy.Item):
    f2 = scrapy.Field() #最新值 指数
    f3 = scrapy.Field() #涨幅
    f12 = scrapy.Field() #板块代码
    f14 = scrapy.Field() #板块名
    f62 = scrapy.Field() #主力净流入
    f66 = scrapy.Field() #超大单净流入
    f69 = scrapy.Field() #超大单净流入净占比
    f72 = scrapy.Field() #大单净流入
    f75 = scrapy.Field() #大单净流入净占比
    f78 = scrapy.Field() #中单净流入
    f81 = scrapy.Field() #中单净流入净占比
    f84 = scrapy.Field() #小单净流入
    f124 = scrapy.Field()#小单净流入净占比
    f184 = scrapy.Field()#主力净流入占比
    f204 = scrapy.Field()#龙头
    f205 = scrapy.Field()#龙头代码

class EastMoneyCompanyInfoItem(scrapy.Item):
    s1 = scrapy.Field()
    s2 = scrapy.Field()
    s3 = scrapy.Field()
    s4 = scrapy.Field()
    s5 = scrapy.Field()
    s6 = scrapy.Field()
    s7 = scrapy.Field()
    s8 = scrapy.Field()
    s9 = scrapy.Field()
    s10 = scrapy.Field()

class EastMoneyBKGPItem(scrapy.Item):
    bk = scrapy.Field()
    f12 = scrapy.Field()
    f14 = scrapy.Field()

class EastMoneyLHBItem(scrapy.Item):
    SCode = scrapy.Field()  #证券代码
    SName = scrapy.Field()  #公司名
    ClosePrice = scrapy.Field() #收盘价
    Chgradio = scrapy.Field()#涨幅
    Dchratio = scrapy.Field()#换手
    JmMoney = scrapy.Field() #净买额
    Turnover = scrapy.Field() #总金额
    Ntransac = scrapy.Field() #总成交手
    Ctypedes = scrapy.Field() #上榜类型
    Smoney = scrapy.Field() #总卖
    Bmoney = scrapy.Field() #总买
    Tdate = scrapy.Field()  #日期
    JmRate = scrapy.Field() #净买占总成交比
    Ltsz = scrapy.Field() #流通市值
    JD = scrapy.Field()  #解读

class EastMoneyGuDongItem(scrapy.Item):
    SecurityCode = scrapy.Field()
    SecurityName = scrapy.Field()
    HolderNum = scrapy.Field()
    PreviousHolderNum = scrapy.Field()
    HolderNumChange = scrapy.Field()
    HolderNumChangeRate = scrapy.Field()
    HolderAvgCapitalisation = scrapy.Field()
    HolderAvgStockQuantity = scrapy.Field()
    EndDate = scrapy.Field()
    PreviousEndDate = scrapy.Field()
    RangeChangeRate = scrapy.Field()
    LatestPrice = scrapy.Field()

class EastMoneyRZRQItem(scrapy.Item):
    Date = scrapy.Field()