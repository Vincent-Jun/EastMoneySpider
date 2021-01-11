# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute("scrapy crawl ConvertibleBond".split())
cmdline.execute("scrapy crawl SinaReal".split())
cmdline.execute("scrapy crawl EastMoneyBK".split())
cmdline.execute("scrapy crawl EastMoneyCompanyInfo".split())
cmdline.execute("scrapy crawl EastMoneyBKGP".split())
cmdline.execute("scrapy crawl EastMoneyLHB".split())