from shop.models import Category, Product
import scrapy
from slugify import slugify
from filters.models import FilterCategory, FilterSelect

class Categories(scrapy.Spider):
    name = "category"

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                yield scrapy.Request(url=category.url, callback=self.parse)

    def parse(self, response):
        category = Category.objects.filter(url=response.url).first()
        for i in response.css('ul.action_filter>li.filter-block'):
            name = i.xpath('header/h4/text()').extract()[0]
            print(name)
            
            fil = FilterCategory.objects.filter(category=category, name=name)
            if not fil:
                fil = FilterCategory(category=category, name=name)
                fil.slug = slugify(name)
                fil.save()
            for f in i.xpath('ul/li/a'):
                url = f.xpath('@href').extract()[0]
                select = f.xpath('text()').extract()[0]
                s = FilterSelect.objects.filter(url=url, filter_category=fil, name=select)
                if not s:
                    s = FilterSelect(url=url, filter_category=fil, name=select)
                s.slug = slugify(select)
                s.save()

