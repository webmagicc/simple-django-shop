from django.core.management.base import BaseCommand, CommandError
from properties.models import CategoryProperty, ProductProperty
from shop.models import Category, Product
from elasticsearch import Elasticsearch




class Command(BaseCommand):

    def handle(self, *args, **options):
        es = Elasticsearch()
        for p in Product.objects.all():
            if p.category:
                slug = p.category.slug
            else:
                continue
            if p.image:
                image = p.image.url
            else:
                image = ''
            doc = {
                'name':p.name,
                'price':p.price,
                'title':p.title,
                'image':image,
                'slug':p.slug,
            }
            filters = p.get_filters()
            for key in filters:
                doc[key] = filters[key]
            res = es.index(index=slug, doc_type='prod', id=p.id, body=doc)
            print("***********************")
            print(doc)
            print(res)
            print("***********************")