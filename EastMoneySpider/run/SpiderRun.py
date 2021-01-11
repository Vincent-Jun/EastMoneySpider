# -*- coding: utf-8 -*-

import scrapy.spiderloader
import scrapy.statscollectors
import scrapy.logformatter
import scrapy.dupefilters
import scrapy.squeues

import scrapy.extensions.spiderstate
import scrapy.extensions.corestats
import scrapy.extensions.telnet
import scrapy.extensions.logstats
import scrapy.extensions.memusage
import scrapy.extensions.memdebug
import scrapy.extensions.feedexport
import scrapy.extensions.closespider
import scrapy.extensions.debug
import scrapy.extensions.httpcache
import scrapy.extensions.statsmailer
import scrapy.extensions.throttle

import scrapy.core.scheduler
import scrapy.core.engine
import scrapy.core.scraper
import scrapy.core.spidermw
import scrapy.core.downloader

import scrapy.downloadermiddlewares.stats
import scrapy.downloadermiddlewares.httpcache
import scrapy.downloadermiddlewares.cookies
import scrapy.downloadermiddlewares.useragent
import scrapy.downloadermiddlewares.httpproxy
import scrapy.downloadermiddlewares.ajaxcrawl
import scrapy.downloadermiddlewares.decompression
import scrapy.downloadermiddlewares.defaultheaders
import scrapy.downloadermiddlewares.downloadtimeout
import scrapy.downloadermiddlewares.httpauth
import scrapy.downloadermiddlewares.httpcompression
import scrapy.downloadermiddlewares.redirect
import scrapy.downloadermiddlewares.retry
import scrapy.downloadermiddlewares.robotstxt

import scrapy.spidermiddlewares.depth
import scrapy.spidermiddlewares.httperror
import scrapy.spidermiddlewares.offsite
import scrapy.spidermiddlewares.referer
import scrapy.spidermiddlewares.urllength

import scrapy.pipelines

import scrapy.core.downloader.handlers.http
import scrapy.core.downloader.contextfactory

import scrapy.core.downloader.handlers.file
import scrapy.core.downloader.handlers.ftp
import scrapy.core.downloader.handlers.datauri
import scrapy.core.downloader.handlers.s3

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


#自己用到的
import time
import schedule
import multiprocessing
from multiprocessing import Process, Queue
from functools import wraps
from twisted.internet import reactor

from EastMoneySpider.run.Statistics import StatisticsHelper
from EastMoneySpider.common.WriteLog import MyLogger
import frozen

logger = MyLogger("RunInfo")

def run_spider_target(spiderName, loopType = 1):
    t = time.localtime()
    if t.tm_hour <= 8 or t.tm_hour >= 16:
        if loopType == 2:
            return
    logger.info("run_spider %s" % spiderName)
    print("run_spider %s" % spiderName)
    try:
        process = CrawlerProcess(get_project_settings())

        deferred = process.crawl(spiderName)
        process.start()
    except Exception as e:
        logger.error(e)


def run_spider(spiderName, loopType = 1):
    try:
        p = Process(target=run_spider_target, args=(spiderName, loopType))
        p.start()
        p.join()
    except Exception as e:
        print(e)

def loopRunSpider(spiderName, loopType, loopTime):
    logger.info("Spider Run %s, LoopTime %s" % (spiderName, loopTime))
    print("Spider Run %s, LoopTime %s" % (spiderName, loopTime))
    for time in loopTime:
        if loopType == 1:
            schedule.every().day.at(time).do(run_spider, spiderName)
        elif loopType == 2:
            schedule.every().hour.at(time).do(run_spider, spiderName, loopType)

def buildHourRange(begin, end, step):
    LoopTime = []
    for item in range(begin, end, step):
        LoopTime.append(":%02d" % item)
    return LoopTime

def statistics():
    statisticsHelper = StatisticsHelper(logger)
    statisticsHelper.bkDayData()
    statisticsHelper.dayData()

def main():
    logger.info('开始检测，等待时间到达，开始执行')
    print('开始检测，等待时间到达，开始执行')
    #run_spider("EastMoneyCompanyInfo")
    #run_spider("EastMoneyBKGP")
    #run_spider("ConvertibleBond")
    #run_spider("SinaReal")
    #run_spider("EastMoneyBK")
    #run_spider("EastMoneyLHB", 1)
    #statistics()

    loopRunSpider("ConvertibleBond", 1, ["09:25", "11:35", "14:55", "15:15"])
    loopRunSpider("SinaReal", 2, buildHourRange(0,60,5))
    loopRunSpider("EastMoneyBK", 2, buildHourRange(0, 60, 5))
    loopRunSpider("EastMoneyLHB", 1, ["17:55", "18:30"])
    schedule.every().day.at("18:00").do(statistics)
    while True:
        schedule.run_pending()
        time.sleep(10)

from EastMoneySpider.common.ParseConfig import getDbConfig
if __name__ == '__main__':
    logger.info(getDbConfig())
    print(getDbConfig())
    multiprocessing.freeze_support()
    main()