from shop.models import Category, Product
import scrapy
from slugify import slugify
from filters.models import FilterCategory, FilterSelect, ProductFilter
from selenium import webdriver
from django.conf import settings
import uuid
from urllib.request import urlretrieve
import time


class ProductFilterSpider(scrapy.Spider):
    name = "product_filter"

    def start_requests(self):
        for category in Category.objects.all():
            for fc in FilterCategory.objects.filter(category=category):
                for fs in FilterSelect.objects.filter(filter_category=fc):
                    driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS)
                    driver.set_window_size(1320, 940)
                    driver.get(fs.url)
                    time.sleep(2)
                    parse_urls = []
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
                            url = fs.url + "page-"+str(i)+"/"
                            parse_urls.append(url)

                    parse_urls.append(fs.url)
                    driver.quit()
                    for url in parse_urls:
                        driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS)
                        driver.set_window_size(1320, 950)
                        driver.get(url)
                        time.sleep(2)
                        for p in driver.find_elements_by_xpath('//div[@class="good-i-t"]/a'):
                            url = p.get_attribute('href')
                            if url:
                                prod = Product.objects.filter(category=category, url=url).first()
                            else:
                                prod = ''

                            if prod:
                                print("PRODUCT "+ prod.name)
                                fp = ProductFilter.objects.filter(product=prod,filter_category=fc).first()
                                if not fp:
                                    fp = ProductFilter(product=prod,filter_category=fc)
                                    fp.save()
                                fp.values.add(fs)
                                fp.save()
                            