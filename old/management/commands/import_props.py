from django.core.management.base import BaseCommand, CommandError
from old.models import *
from shop.models import *
from properties.models import *



class Command(BaseCommand):

    def handle(self, *args, **options):
        
        
        for c in ShopPropertyfilters.objects.using('old').all():
            category_id = c.category_id
            category = Category.objects.filter(pk=category_id).first()
            prop = c.property.name
            np = CategoryProperty.objects.filter(category=category,name=prop).first()
            if not np:
                np = CategoryProperty(category=category,name=prop)
                np.save()
            for sp in ShopPropertyproduct.objects.using('old').filter(property=c.property):
                npp = ProductProperty.objects.filter(category_property=np,product_id=sp.product_id)
                p = Product.objects.filter(pk=sp.product_id).first()
                if not npp and p:
                    npp = ProductProperty(category_property=np, value=sp.value, product=p)
                    npp.save()
                    print(npp.id)
            
            