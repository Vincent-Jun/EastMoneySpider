# -*- coding: utf-8 -*-
from EastMoneySpider.AnalysisTool.TableBuild.BKTable import getBKTable

def saveHtml(file_name,file_content):
    with open(file_name+'.html','w') as f:
        f.write(file_content)

if __name__ == '__main__':
    saveHtml("BK", getBKTable())