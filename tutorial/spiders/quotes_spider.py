from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {"tutorial.middlewares.QuotesSpiderMiddleware": 543}
    }

    def start_requests(self):
        urls = [
            'https://www.ups.com/cn/zh/support/shipping-support/shipping-costs-rates/fuel-surcharges.page',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       # page = response.url.split("/")[-2]
       # s =  response.xpath('//div[@class="container"]/div/div/h1/a/text()')[0].extract()
       # d = response.xpath('//div[@class="container"]//a/text()')[0].extract()
        # <div class="container">
        #  <div class="row header-box">
        #        <div class="col-md-8">
        #         <h1>
        #           <a href="/" style="text-decoration: none">Quotes to Scrape</a>
        #       </h1>
        #    </div>
        #   <div class="col-md-4">
        #       <p>

        #           <a href="/login">Login</a>
        #
        #       </p>

        #   </div>
        #   </div>

        # //div//a 表示直接读取div下面所有到a标签（子 孙子***） 元素下只要满足对应到就行  可以直接到最后到元素
        # / 表示一级 一级 到读取  /div/div 只能读取当前div的下级(子级)div
       # print(s,d,"aaa")
         filename = f'quotes.html'

         res = response.xpath('//div[@id="RevenueSurchargeHistory"][1]//tbody/tr[1]/td[2]/text()').extract()

         # Path(filename).write_bytes(res)
         # self.log(f'Saved file {filename}')
         print(res[0],"aaaaaa")