data = '''
[settings]
default = EastMoneySpider.settings

[deploy]
#url = http://localhost:6800/
project = EastMoneySpider
'''

with open('scrapy.cfg', 'w') as f:
    f.write(data)