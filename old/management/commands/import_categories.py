from django.core.management.base import BaseCommand, CommandError
from old.models import ShopCategory
from shop.models import Category



class Command(BaseCommand):

    def handle(self, *args, **options):
        for c in ShopCategory.objects.using('old').all().order_by('-parent_id'):
            category = Category.objects.filter(slug=c.slug).first()
            if not category:
                category = Category(pk=c.pk)

            category.name = c.name
            category.slug = c.slug
            category.title = c.title
            category.description = c.metadesc
            category.keywords = c.metakey
            if c.parent_id:
                parent = Category.objects.filter(pk=c.parent_id).first()
                if parent:
                    category.parent = parent
            category.image = c.image
            category.save()
            print(category.id)
            