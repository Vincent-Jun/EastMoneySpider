xcopy  /y .\EastMoneySpider\config\*.* .\Release\config\
pyi-makespec -F SpiderRun.py
pyinstaller -F --add-data=mime.types;scrapy --add-data=VERSION;scrapy --add-data=EastMoneySpider/*py;EastMoneySpider --add-data=EastMoneySpider/spiders/*.py;EastMoneySpider/spiders --runtime-hook=generate_cfg.py --distpath="./Release/bin" EastMoneySpider/run/SpiderRun.py