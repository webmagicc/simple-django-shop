from shop.models import Category, Product
from django.core.management.base import BaseCommand, CommandError
from properties.models import CategoryProperty, ProductProperty
from django.conf import settings
import uuid
from urllib.request import urlretrieve
import time
from decimal import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests
import threading
from shop_scraper.phantom import get_driver
from pyquery import PyQuery as pq

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


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("&&&&&&&&&&&&&&&&& START &&&&&&&&&&&&&&&&&&&&&&&")
        i = 1
        for item in Product.objects.all():
            print("PRODUCT "+ str(item.name))
            category = item.category
            if item.url:
                time.sleep(1)
                exec("t%s = threading.Thread(target=self.get_page, args=(item,))" % str(i))
                exec("t%s.start()" % str(i))
                print("START t%s" % str(i))
                i += 1
                if i % 5 == 0:
                    time.sleep(20)
                    print("Sleep 20")
                elif i % 32 ==0:
                    time.sleep(40)
                    print("Sleep 40")
                elif i % 52 ==0:
                    time.sleep(60)
                    print("Sleep 60")
                elif i % 82 ==0:
                    time.sleep(80)
                    print("Sleep 80")
                elif i % 142 ==0:
                    time.sleep(120)
                    print("Sleep 120")
                elif i % 211 ==0:
                    time.sleep(180)
                    print("Sleep 180")
                elif i % 311 ==0:
                    time.sleep(240)
                    print("Sleep 240")
    
    def get_page(self, item):
        driver = get_driver()
        driver.implicitly_wait(10)
        driver.get(item.url)
        driver.find_element_by_xpath("//a[@href='#good-spec-tab']").click()
        time.sleep(2)
        html = driver.page_source
        exec("p%s = threading.Thread(target=self.parse, args=(item,html))" % str(item.id))
        exec("p%s.start()" % str(item.id))
        print("START p%s" % str(item.id))
        driver.quit()

    def parse(self, item, html):
        page = pq(html)
        title = page('title').html()
        print("*** TITLE "+title)
        try:
            price = page('.good-price strong').html()
            
        except:
            price = 0.00
        print("*** PRICE "+str(price))

        if not item.image:
            img = page('.fotorama__img:first').attr('src')
            
            new_image = make_upload_path()
            print(make_save_name(new_image))
            if img:
                img_temp = NamedTemporaryFile(delete=True)
                r = requests.get(img)
                img_temp.write(r.content)
                img_temp.flush()
                item.image.save(new_image.split('/')[-1], File(img_temp), save=True)
                
        if price:
            item.price = Decimal(price)
        
        
        
        for i in page('.dl-horizontal div'):
            try: 
                name = i('dt').html()
            except:
                name = ""
            try:
                value = i('dd').html()
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
                
