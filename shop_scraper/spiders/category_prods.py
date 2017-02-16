from shop.models import Category, Product
import scrapy
from slugify import slugify
from filters.models import FilterCategory, FilterSelect

class Categories(scrapy.Spider):
    name = "category_product"

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                yield scrapy.Request(url=category.url, callback=self.get_pagination)

    def get_pagination(self, response):
    	res = []
    	res.append(response.url)
    	
