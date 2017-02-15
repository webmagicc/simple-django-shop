from shop.models import Category, Product
import scrapy
from slugify import slugify
from properties.models import CategoryProperty

class CategoryProperty(scrapy.Spider):
    name = "category_property"
    category = ''

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                yield scrapy.Request(url=category.url, callback=self.parse)

    def parse(self, response):
        category = Category.objects.filter(url=response.url).first()
        self.category = category
        try:
            product_link = response.xpath('//*[@id="itemsarticle"]/section[1]/div/div[1]/a/@href').extract()[0]
        except:
            product_link = ""

        
        if product_link:
            if 'https://' in product_link:
                product_link =  product_link +'#harakteristiki'
            else:
                product_link = "https://www.microsoftstore.ru" + product_link +'harakteristiki/'
            print(product_link)
            yield scrapy.Request(url=product_link, callback=self.parse_prod)

    def parse_prod(self, response):
        for i in response.css('div.control-group'):
            name = i.xpath('div[@class="control-label bn-properties-label"]/span[@class="properties__label-text"]/text()').extract()
            if name:
                name = name[0]
                name = name.strip()
                cp = CategoryProperty.objects.filter(category=self.category, name=name).first()
                if not cp:
                    cp = CategoryProperty(category=self.category, name=name)
                    cp.save()

                




        
