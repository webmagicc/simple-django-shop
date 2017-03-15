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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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
                dcap = dict(DesiredCapabilities.PHANTOMJS)
                dcap["phantomjs.page.settings.userAgent"] = (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
                    "(KHTML, like Gecko) Chrome/15.0.87"
                )
                driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS, desired_capabilities=dcap)
                
                driver.set_window_size(1320, 940)
                driver.get(item.url)
                time.sleep(5)
                price = driver.find_element_by_xpath('//span[@class="bn-product-baseprice"]').text
                price = price.replace('\u2009','')
                price = price.replace('\u2009р.','')
                price = price.replace(' ','')
                price = price.replace('p','')
                price = price.replace('.','')
                price = price.replace('р','')
                img = driver.find_element_by_xpath("//div[@class='swiper-slide swiper-slide-active']/img").get_attribute('src')
                new_image = make_upload_path()
                print(make_save_name(new_image))
                if img:
                    urlretrieve(img,new_image)
                    item.image = make_save_name(new_image)
                if price:
                    item.price = Decimal(price)
                print(item.image)
                print(item.price)
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
                driver.quit()

