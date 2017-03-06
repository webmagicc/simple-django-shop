from shop.models import Category, Product
import scrapy
from slugify import slugify
from filters.models import FilterCategory, FilterSelect


class CategoryProductSpider(scrapy.Spider):
    name = "category_product_spider"

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                yield scrapy.Request(url=category.url, callback=self.get_pagination)

    def get_pagination(self, response):
        res = []
        res.append(response.url)
        for li in response.xpath("//div[@class='pagination']/ul/li"):
            a = li.xpath("a[1]/@href").extract_first()
            print(a)
            
            if a:
                a = "https://www.microsoftstore.ru"+a
                print(a)
                yield scrapy.Request(url=a, callback=self.parse)
            
        self.parse(response)


    def parse(self, response):
    	category_name = response.xpath("//h1/span/text()").extract_first()
    	print(category_name)
    	category = Category.objects.filter(name=category_name).first()
    	print(category)
    	for p in response.xpath("//div[@class='product-cell__link']"):
    		name = p.xpath("div[@class='product-cell__header bn-title']/h2/a/text()").extract_first()
    		link = p.xpath('div[1]/a/@href').extract_first()
    		if name and link and category:
    			slug = slugify(name)
    			url = "https://www.microsoftstore.ru"+link
    			prod = Product.objects.filter(name=name, url=url, category=category, slug=slug).first()
    			if not prod:
    				prod = Product(name=name, url=url, category=category, slug=slug)
    				prod.save()
    		print(name)
    		print(link)

        
