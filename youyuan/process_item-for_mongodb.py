# !/usr/bin/python
# -*- encoding: utf-8 -*-
# @author:spider1998
#!/usr/bin/env python
import redis
import pymongo
import json

def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host = "127.0.0.1", port = 6379, db = "0")

    # 创建MongoDB数据库连接
    mongocli = pymongo.MongoClient(host = "127.0.0.1", port = 27017)
    mongocli.admin.authenticate("admin","123")

    # 创建mongodb数据库名称
    dbname = mongocli["youyuan"]
    # 创建mongodb数据库youyuan的表名称
    sheetname = dbname["xian_18_33_mm"]
    offset = 0

    while True:
        # redis 数据表名 和 数据
        source, data = rediscli.blpop("yy:items")
        offset += 1
        # 将json对象转换为Python对象
        data = json.loads(data)
        # 将数据插入到sheetname表里
        sheetname.insert(data)
        print offset

if __name__ == "__main__":
    process_item()
