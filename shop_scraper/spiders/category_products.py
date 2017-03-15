from shop.models import Category, Product
import scrapy
from slugify import slugify
from filters.models import FilterCategory, FilterSelect


class CategoryProductSpider(scrapy.Spider):
    name = "category_product_spider"

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS)
                driver.set_window_size(1320, 950)
                driver.get(category.url)
                time.sleep(5)
                try:
                    pagination = driver.find_elements_by_xpath('//ul[@class="pagination"]/li')
                except:
                    pagination = ""
                if len(pagination)>2:
                    last = pagination[-2].text
                else:
                    last = ""
                if last:
                    page_list = range(int(last)+1)
                    for i in page_list:
                        if i == 0:
                            continue
                        url = category.url + "page-"+str(i)+"/"



    


    def parse(self, response):
        category_name = response.xpath("//h1/span/text()").extract_first()
        print(category_name)
        category = Category.objects.filter(name=category_name).first()
        print(category)
        for p in response.xpath("//div[@class='product-cell__link']"):
            name = p.xpath("div[@class='product-cell__header bn-title']/h2/a/text()").extract_first()
            name = name.strip()
            link = p.xpath('div[1]/a/@href').extract_first()
            link = link.strip()
            if name and link and category:
                slug = slugify(name)
                url = "https://www.microsoftstore.ru"+link
                prod = Product.objects.filter(name=name, url=url, category=category, slug=slug).first()
                if not prod:
                    prod = Product(name=name, url=url, category=category, slug=slug)
                    prod.save()
            print(name)
            print(link)

        
