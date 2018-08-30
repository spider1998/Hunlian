# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
BOT_NAME = 'youyuan'

SPIDER_MODULES = ['youyuan.spiders']
NEWSPIDER_MODULE = 'youyuan.spiders'

#USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'youyuan.pipelines.YouyuanPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#REDIS_HOST = "192.168.60.1"
#REDIS_PORT = 6379

#LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
#DOWNLOAD_DELAY = 1
