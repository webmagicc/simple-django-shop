from shop.models import Category, Product
import scrapy
from slugify import slugify
from filters.models import FilterCategory, FilterSelect
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from decimal import *
from selenium import webdriver
from django.conf import settings

class CategoryFilters(scrapy.Spider):
    name = "category_filters"

    def start_requests(self):
        for category in Category.objects.all():
            if category.url:
                driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS)
                driver.set_window_size(1320, 950)
                driver.get(category.url)
                time.sleep(5)
                
                brand = FilterCategory.objects.filter(name='Brand', category=category).first()
                if not brand:
                    brand = FilterCategory(name='Brand', category=category)
                    brand.save()
                for b in driver.find_elements_by_css_selector('.brand a.leftmenu'):
                    link = b.get_attribute('href')
                    name = b.text
                    slug = slugify(name)
                    if link and name:
                        fs = FilterSelect.objects.filter(filter_category=brand,name=name, url=link).first()
                        if not fs:
                            fs = FilterSelect(filter_category=brand, slug=slug, name=name, url=link)
                            fs.save()
                for b in driver.find_elements_by_xpath('//div[@class="filter-box"]'):
                    print("***** START ********")
                    try:
                        fname = b.find_element_by_xpath('header/strong/a').text
                    except:
                        print("**** ERROR FNAME")
                        continue
                    print("*****" + fname)
                    fc = FilterCategory.objects.filter(name=fname, category=category).first()
                    if not fc:
                        fc = FilterCategory(name=fname, category=category)
                        fc.save()

                    for s in b.find_elements_by_xpath('div[1]/div'):
                        print("***** WALK BY FILTER SELECT ******")
                        fid = s.find_element_by_xpath('label').get_attribute('for')
                        print("**** FID "+fid)
                        name = s.find_element_by_xpath('label/i').text
                        print("**** NAME "+name)
                        url = "https://tovarok.com.ua/planshety/?"+fid+"=1"
                        slug = slugify(name)
                        print("**** NAME "+slug)
                        if name:
                            fs = FilterSelect.objects.filter(filter_category=fc,name=name, url=url).first()
                            if not fs:
                                fs = FilterSelect(filter_category=fc, slug=slug, name=name, url=url)
                                fs.save()








        

    