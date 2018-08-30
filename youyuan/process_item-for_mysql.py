# !/usr/bin/python
# -*- encoding: utf-8 -*-
# @author:spider1998
import redis
import MySQLdb
import json

def process_item():
    rediscli = redis.Redis(host = "127.0.0.1",port = 6379,db = 0)
    mysqlcli = MySQLdb.connect(host = "127.0.0.1",port = 3306,user = "root",passwd = "123456",db = "youyuan",charset = "utf8")
    offset = 0
    while True:
        source,data = rediscli.blpop("yy:items")
        item = json.loads(data)
        #创建游标对象
        cursor = mysqlcli.cursor()
        cursor.execute("insert into xian_18_32_mm (username,header_url,general_info,detailed,appearance,situation,hobby,selfhood,images_urls,source_url,source) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[item['username'],item['header_url'],item['general_info'],item['detailed'],item['appearance'],item['situation'],item['hobby'],item['selfhood'],item['images_url'],item['source_url'],item['source']])
        mysqlcli.commit()
        cursor.close()
        offset += 1
        print offset



if __name__ == "__main__":
    process_item()