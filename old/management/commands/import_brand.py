from django.core.management.base import BaseCommand, CommandError
from old.models import ShopCategory, ShopProduct, ShopBrand
from shop.models import Category, Product
from filters.models import FilterCategory, FilterSelect, ProductFilter
from slugify import slugify



class Command(BaseCommand):

    def handle(self, *args, **options):
        
        for c in ShopProduct.objects.using('old').all():
            b = c.brand
            try:
                c_id = c.category.id
            except:
                continue
            category = Category.objects.filter(pk=c_id).first()
            fc = FilterCategory.objects.filter(category=category,slug='brand').first()
            if not fc:
                fc = FilterCategory(category=category,slug='brand',name="Производитель")
                fc.save()
            fs = FilterSelect.objects.filter(filter_category=fc,name=b.name).first()
            if not fs:
                if not b.slug:
                    slug = slugify(b.name)
                else:
                    slug = b.slug
                fs = FilterSelect(filter_category=fc,name=b.name,slug=slug)
                fs.save()

            p = Product.objects.filter(pk=c.id).first()
            if not p:
                continue
            fp = ProductFilter.objects.filter(product=p,filter_category=fc).first()
            if not fp:
                fp = ProductFilter(product=p,filter_category=fc)
                fp.save()
            fp.values.add(fs)
            fp.save()
            print(b.name)


            