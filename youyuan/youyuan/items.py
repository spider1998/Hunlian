# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class YouyuanItem(Item):
    #姓名
    username = Field()
    #头像
    header_url = Field()
    #大体信息
    general_info = Field()
    #详细信息
    detailed = Field()
    #外貌
    appearance = Field()
    #现状
    situation = Field()
    #爱好
    hobby = Field()
    #个性
    selfhood = Field()
    #相册
    images_url = Field()
    #主页
    source_url = Field()
    #数据来源网站
    source = Field()

