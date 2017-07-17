from django.core.management.base import BaseCommand, CommandError
from old.models import ShopCategory, ShopProduct
from shop.models import Category, Product



class Command(BaseCommand):

    def handle(self, *args, **options):
        d = Product.objects.all()
        d.delete()
        for c in ShopProduct.objects.using('old').all():
            category = Category.objects.filter(pk=c.category_id).first()
            prod = Product.objects.filter(category=category,slug=c.slug).first()
            if not prod:
                prod = Product(pk=c.pk)
            prod.name = c.name
            prod.category = category
            prod.slug = c.slug
            prod.title = c.title
            prod.description = c.metadesc
            prod.keywords = c.metakey
            prod.price = c.price
            prod.image = c.image
            prod.description = c.description
            prod.full_text = c.full_text
            prod.save()
            print(prod.id)
            