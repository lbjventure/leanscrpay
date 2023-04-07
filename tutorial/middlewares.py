# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

import requests
import scrapy
from scrapy import signals

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class TutorialSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i



    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class LoginMiddleware(object):

    _cookies = None
    _browser = None
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.cookies = None

    def __del__(self):
        self.browser.quit()
    def process_request(self,request,spider):
        print("aaaaaname",spider.name)

        if spider.name=="loginspider" :
            print("cccv",request.url.find("login"))
            if request.url.find("login")==-1  and self.cookies is None:
                self.browser.get(request.url)
                time.sleep(3)
                print("login ",request.url)
                email = self.browser.find_element(by = By.XPATH,value = '//input[@name="email"]')
                password = self.browser.find_element(by = By.XPATH,value='//input[@name="password"]')


                time.sleep(1)

                email.send_keys("support@**.com")
                password.send_keys("***~")
                click = self.browser.find_element(by=By.XPATH,value='//button[@class="btn btn-primary"]')
                click.click()
                time.sleep(5)
                self.cookies = self.browser.get_cookies()
                print("cooo=====",self.cookies)
                res = scrapy.http.HtmlResponse(url=request.url, body=self.browser.page_source.encode('utf-8'),
                                               encoding='utf-8',
                                               request=request, status=200)
                print("33333")

                return res
            else:
                print("cooo=====", self.cookies)
                req = requests.session()
                for cookie in self.cookies:
                    req.cookies.set(cookie['name'],cookie["value"])

                req.headers.clear()
                newpage = req.get(request.url)
                time.sleep(3)


                time.sleep(3)

                res = scrapy.http.HtmlResponse(url=request.url, body=newpage.text,
                           encoding='utf-8',
                           request=request, status=200)
                print("55555")

                return res
        else:
            print("tet")
            pass



class QuotesSpiderMiddleware(object):

    _timeout = 1

    _driver = None

    _wait = None

    _option = None

    def __init__(self):


        self.timeout = 3


        #  self.driver.implicitly_wait(self,15)
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=self.option)
        # self.driver.maximize_window()
        # request.meta.sefdefault("download_timeout",self._timeout)
        self.wait = WebDriverWait(self.driver, 10)



    def __del__(self):
        self.driver.quit()
    def process_request(self, request, spider):

        if spider.name=="quotes":


            print("afddwfsdfsdfdsfdsf",self.timeout)

            try:
                self.driver.get(request.url)


                print("1111111")
                #self.wait.until(EC.presence_of_element_located((By.ID,"RevenueSurchargeHistory")),message="aaaaddadfasdfsdfccccc")
                self.wait.until(lambda x: x.find_element(By.ID, "RevenueSurchargeHistory"))
                print("222222")
                res = scrapy.http.HtmlResponse(url=request.url, body=self.driver.page_source.encode('utf-8'), encoding='utf-8',
                                     request=request, status=200)
                print("33333")


                return res
            except TimeoutError:
                print("55555")
                return None
            finally:
                pass



class TutorialDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.


        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
