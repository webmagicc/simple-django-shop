from shop.models import Category
import scrapy
from slugify import slugify

class Categories(scrapy.Spider):
    name = "categories"

    def start_requests(self):
        urls = [
            'https://www.microsoftstore.ru/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
    	for i in response.css('ul.top-nav>li>a'):
    		try: 
	    		name = i.xpath('text()').extract()[0]
	    		url = i.xpath('@href').extract()[0]
	    		url = "https://www.microsoftstore.ru" + url
	    	except:
	    		name = ""
	    		url = ""
	    	if name and url:
	    		category = Category.objects.filter(name=name).first()
	    		if not category:
	    			slug = slugify(name)
	    			category = Category(name=name, slug=slug, url=url)
	    			category.save()
