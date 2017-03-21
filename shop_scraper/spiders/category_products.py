from shop.models import Category, Product
import scrapy
from django.utils.text import slugify
from filters.models import FilterCategory, FilterSelect
from selenium import webdriver
from django.conf import settings
import time


class CategoryProducts(scrapy.Spider):
    name = "category_products"

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                parse_urls = []
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
                        parse_urls.append(url)

                parse_urls.append(category.url)
                driver.quit()
                for url in parse_urls:
                    driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS)
                    driver.set_window_size(1320, 950)
                    driver.get(url)
                    time.sleep(5)
                    for p in driver.find_elements_by_xpath('//div[@class="good-i-t"]/a'):
                        name = p.text
                        url = p.get_attribute('href')
                        slug = slugify(name)
                        prod = Product.objects.filter(category=category, slug=slug, name=name).first()
                        print("***"+name)
                        print("***"+url)
                        print("***"+slug)

                        if not prod:
                            prod = Product(category=category, slug=slug, name=name, url=url)
                            prod.save()
                        else:
                            prod.url = url
                            prod.save()




    


    

        
