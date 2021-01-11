# -*-coding:utf-8-*-
import pymysql


class MySqlHelper(object):
    mySqlHelper = None

    # 单例
    def __new__(cls, *args, **kwargs):
        if not cls.mySqlHelper:
            cls.mySqlHelper = super().__new__(cls)
        return cls.mySqlHelper

    def __init__(self, host, username, password, db, charset='utf8', port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port
        self.mysqlConnect = None
        self.cursor = None

    def __del__(self):
        if self.mysqlConnect:
            self.close()

    def connect(self):
        self.mysqlConnect = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                            db=self.db, charset=self.charset)
        self.cursor = self.mysqlConnect.cursor()

    def close(self):
        self.cursor.close()
        self.mysqlConnect.close()

    def get(self, sql, params=()):
        list_data = ()
        try:
            if self.mysqlConnect is None:
                self.connect()
            self.cursor.execute(sql, params)
            list_data = self.cursor.fetchall()
        except Exception as e:
            print(sql)
            print(e)
        return list_data

    def execute(self, sql, params=()):
        count = 0
        try:
            if self.mysqlConnect is None:
                self.connect()
            count = self.cursor.execute(sql, params)
            self.mysqlConnect.commit()
        except Exception as e:
            print(sql)
            print(e)

        return count

