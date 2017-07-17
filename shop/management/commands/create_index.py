from django.core.management.base import BaseCommand, CommandError
from properties.models import CategoryProperty, ProductProperty
from shop.models import Category, Product
from elasticsearch import Elasticsearch




class Command(BaseCommand):

    def handle(self, *args, **options):
        es = Elasticsearch()
        count = 0
        for p in Product.objects.all().order_by('id')[4000:]:
            a = es.search(index='products',body={"query": {"match": {"product_id":p.id}}})
            
            if p.category:
                slug = p.category.slug
            else:
                continue
            if p.image:
                image = p.image.url
            else:
                image = ''
            count += 1
            doc = {
                'name':p.name,
                'product_id':p.id,
                'price':p.price,
                'title':p.title,
                'image':image,
                'slug':p.slug,
                'created_at':p.created_at,
                'updated_at':p.updated_at,
            }
            filters = p.get_filters()
            for key in filters:
                doc[key] = filters[key]
            
            res = es.index(index='products', doc_type=slug,  body=doc)
            print("***********************")
            print("prod id "+ str(p.id))
            print("count "+str(count))
            print("***********************")