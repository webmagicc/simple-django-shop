from properties.models import CategoryProperty, ProductProperty
from shop.models import Category, Product
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):

    def handle(self, *args, **options):
    	for p in Product.objects.all():
    		for pp in ProductProperty.objects.filter(product=p):
    			if ProductProperty.objects.filter(product=p, category_property=pp.category_property).count()>1:
    				pd = ProductProperty.objects.filter(product=p, category_property=pp.category_property,value='--')
    				pd.delete()
