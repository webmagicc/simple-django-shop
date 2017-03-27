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
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests

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
        print("&&&&&&&&&&&&&&&&& START &&&&&&&&&&&&&&&&&&&&&&&")
        for item in Product.objects.all():
            print("PRODUCT "+ str(item.name))
            category = item.category
            if item.url:
                
                driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS)
                
                driver.set_window_size(1320, 940)
                driver.get(item.url)
                time.sleep(5)
                title = driver.find_element_by_xpath('//title').text
                print("*** TITLE "+title)
                try:
                    price = driver.find_element_by_xpath('//div[@class="good-price"]/strong').text
                except:
                    price = 0.00
                print("*** PRICE "+str(price))

                if not item.image:
                
                    img = driver.find_elements_by_xpath("//*[@class='fotorama__img']")[0].get_attribute('src')
                    new_image = make_upload_path()
                    print(make_save_name(new_image))
                    if img:
                        img_temp = NamedTemporaryFile(delete=True)
                        r = requests.get(img)
                        img_temp.write(r.content)
                        img_temp.flush()
                        item.image.save(new_image.split('/')[-1], File(img_temp), save=True)
                        #urlretrieve(img,new_image)
                        #item.image = make_save_name(new_image)
                        #item.image.path = new_image
                if price:
                    item.price = Decimal(price)
                
                
                driver.find_element_by_xpath("//a[@href='#good-spec-tab']").click()
                time.sleep(2)
                for i in driver.find_elements_by_xpath("//*[@class='dl-horizontal']/div"):
                    try: 
                        name = i.find_element_by_xpath("dt").text
                    except:
                        name = ""
                    try:
                        value = i.find_element_by_xpath("dd").text
                    except:
                        value = ""
                    name = name.strip()
                    value = value.strip()
                    print("*** NAME PROP "+name)
                    print("*** VALUE PROP "+value)

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

