# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from youyuan.items import YouyuanItem


#class YySpider(CrawlSpider):
class YySpider(RedisCrawlSpider):
    name = 'yy'
    #allowed_domains = ['iqingren.com']
    redis_key = "yyspider:start_urls"
    #获取动态域范围
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(YySpider, self).__init__(*args, **kwargs)

    #start_urls = ['http://www.iqingren.com/search?sex=0&startAge=18&endAge=32&province=%E9%99%95%E8%A5%BF&city=%E8%A5%BF%E5%AE%89&ispic=1']
    #西安18岁-32岁每一页链接
    pagelinks = LinkExtractor(allow = (r"/search.*page=\d+"))
    #个人主页
    profilelinks = LinkExtractor(allow = (r"iqingren.com/User/.*.html"))

    rules = (
        Rule(pagelinks,follow=True),
        Rule(profilelinks,callback = "parse_item"),
    )

    def parse_item(self, response):
        item = YouyuanItem()
        # 姓名
        item['username'] = self.get_username(response)
        # 头像
        item['header_url'] = self.get_header_url(response)
        # 大体信息
        item['general_info'] = self.get_general_info(response)
        # 详细信息
        item['detailed'] = self.get_detailed(response)
        # 外貌
        item['appearance'] = self.get_appearance(response)
        # 现状
        item['situation'] = self.get_situation(response)
        # 爱好
        item['hobby'] = self.get_hobby(response)
        # 个性
        item['selfhood'] = self.get_selfhood(response)
        # 相册
        item['images_url'] = self.get_image_url(response)
        # 主页
        item['source_url'] = response.url
        # 数据来源网站
        item['source'] = "iqingren"
        yield item

    def judge(self, params):
        if len(params):
            params = params[0]
        else:
            params = "NULL"
        return params


    def get_username(self,response):
        username = response.xpath('/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/a/text()').extract()
        return self.judge(username).strip()

    def get_header_url(self,response):
        header_url = response.xpath('//div[@class="column info"]/div[1]/div[1]/div/@style').extract()
        header_url = self.judge(header_url)
        return header_url.split(" ")[1].replace("]","").strip()

    def get_general_info(self,response):
        general_info = response.xpath('//div[@class="column padding_20_t padding_10_b line_h_26 rgb_666"]/div/text()').extract()
        general = []
        if len(general_info):
            for i in range(0, len(general_info)):
                gen = general_info[i].strip()
                general.append(gen)
        else:
            general = "NULL"
        return ",".join(general)

    def get_detailed(self,response):
        detail = response.xpath('//div[@class="column padding_10_b padding_10_t line_h_26 rgb_666"]/div/text()').extract()
        data = []
        if len(detail):
            for i in range(0, len(detail)):
                de = detail[i].strip()
                data.append(de)
        else:
            data= "NULL"
        return ",".join(data)

    def get_appearance(self,response):
        appearance = response.xpath('//div[@class="column margin_20_b"][1]/div/div[2]/text()').extract()
        return self.judge(appearance).replace(" ", "").strip()

    def get_situation(self,response):
        situation = response.xpath('//div[@class="column margin_20_b"][2]/div/div[2]/text()').extract()
        return self.judge(situation).replace(" ", "").strip()

    def get_hobby(self,response):
        situation = response.xpath('//div[@class="column margin_20_b"][3]/div/div[2]/text()').extract()
        return self.judge(situation).replace(" ", "").strip()

    def get_selfhood(self,response):
        situation = response.xpath('//div[@class="column margin_20_b"][4]/div/div[2]/text()').extract()
        return self.judge(situation).replace(" ", "").strip()

    def get_image_url(self,response):
        image_url = response.xpath('//ul[@class="photo_list"]/li/a/@style').extract()
        image = []
        if len(image_url):
            for i in range(0,len(image_url)):
                img = image_url[i].split(" ")[1].strip()
                image.append(img)
        else:
            image = "NULL"
        return ",".join(image)
