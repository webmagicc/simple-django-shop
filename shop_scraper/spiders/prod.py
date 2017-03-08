from shop.models import Category, Product
import scrapy
from slugify import slugify
from properties.models import CategoryProperty, ProductProperty
from selenium import webdriver
from django.conf import settings
import uuid
from urllib.request import urlretrieve
import time
from decimal import *

def make_upload_path():
    """
    Create unique name for image or file.
    """
    new_name = str(uuid.uuid1())
    
    filename = new_name + '.jpg'
    return u"%s/%s/%s" % (settings.MEDIA_ROOT,settings.SHOP_IMAGE_DIR, filename)
def make_save_name(name):
    
    parts = name.split('/')
    return u"%s/%s" % (settings.SHOP_IMAGE_DIR, parts[-1])

class Prod(scrapy.Spider):
    name = "prod"
    

    def start_requests(self):
        for item in Product.objects.all().order_by('-updated_at'):
            category = item.category
            if item.url:
                driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS)
                driver.set_window_size(1280, 640)
                driver.get(item.url)
                price = driver.find_element_by_xpath('//span[@class="bn-product-baseprice"]').text
                price = price.replace('\u2009','')
                price = price.replace('\u2009р.','')
                price = price.replace(' ','')
                price = price.replace('p','')
                price = price.replace('.','')
                price = price.replace('р','')
                img = driver.find_element_by_xpath("//div[@class='swiper-slide swiper-slide-active']/img").get_attribute('src')
                new_image = make_upload_path()
                if img:
                    urlretrieve(img,new_image)
                    item.image = make_save_name(new_image)
                if price:
                    item.price = Decimal(price)
                new_url = item.url+'harakteristiki/'
                driver.get(new_url)
                time.sleep(2)
                for i in driver.find_elements_by_xpath("//div[@class='control-group']"):
                    try: 
                        name = i.find_element_by_xpath("div[1]/span").text
                    except:
                        name = ""
                    try:
                        value = i.find_element_by_xpath("div[2]/span").text
                    except:
                        value = ""
                    name = name.strip()
                    value = value.strip()
                    if name and value:
                        cp = CategoryProperty.objects.filter(category=category, name=name).first()
                        if not cp:
                            cp = CategoryProperty(category=category, name=name)
                            cp.save()
                        p = ProductProperty.objects.filter(category_property=cp,
                                                            value=value,
                                                            product=item)
                        if not p:
                            p = ProductProperty(category_property=cp,
                                                value=value,
                                                product=item)
                            p.save()

