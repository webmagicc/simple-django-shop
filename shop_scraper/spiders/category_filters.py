from shop.models import Category, Product
import scrapy
from slugify import slugify

class Categories(scrapy.Spider):
    name = "category"

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                yield scrapy.Request(url=category.url, callback=self.parse)

    def parse(self, response):
        for i in response.css('ul.action_filter>li.filter-block'):
            name = i.xpath('header/h4/text()').extract()[0]
            print(name)
