import scrapy

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class LoginspiderSpider(scrapy.Spider):
    name = "loginspider"
    allowed_domains = ["**.com"]
    start_urls = [
        # "http://www.wmsby.com/",
          "http://www.**.com/admin/goods/goodslist?searchvar=%7B%22sku%22:%22343242343243242342222%22%7D"
    ]

    #可以自定义配置
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{"tutorial.middlewares.LoginMiddleware": 545}
    }





    def parse(self, response):
         print(response.body.decode("utf-8","ignore"))
        #  url = "http://www.wmsby.com/admin/goods/goodslist?searchvar=%7B%22sku%22:%22343242343243242342222%22%7D"
        #  yield scrapy.Request(url,callback=self.goods)
        #  pass






    def goods(self,response):
        print(response.body)
        pass