# -*-coding:utf-8-*-

from configparser import ConfigParser
import os.path
#解析Setting.ini


def getDbConfig():
    iniParser = ConfigParser()
    dbini_path = os.path.dirname(os.getcwd()) + '/config/Setting.ini'
    iniParser.read(dbini_path)
    dbConfig = []
    dbConfig.append(iniParser.get("Mysql", "Host"))
    dbConfig.append(iniParser.get("Mysql", "User"))
    dbConfig.append(iniParser.get("Mysql", "Pwd"))
    dbConfig.append(iniParser.get("Mysql", "Db"))
    return dbConfig

if __name__ == '__main__':
    print(getDbConfig())