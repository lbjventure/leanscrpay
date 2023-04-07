import scrapy


class LoginspiderSpider(scrapy.Spider):
    name = "loginspider"
    allowed_domains = ["wmsby.com"]
    start_urls = ["http://www.wmsby.com/"]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"email":"****","password":"***"},
            callback = self.afterlogn
        )

        pass

    def afterlogn(self,response):

        url  = "http://****/admin/goods/goodslist?searchvar=%7B%22sku%22:%22343242343243242342222%22%7D"
        yield scrapy.Request(url,callback=self.goods)
        print(response)

    def goods(self,response):
        print(response.body)