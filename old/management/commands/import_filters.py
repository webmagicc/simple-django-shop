from django.core.management.base import BaseCommand, CommandError
from old.models import *
from shop.models import *
from properties.models import *
from filters.models import *
from slugify import slugify



class Command(BaseCommand):

    def handle(self, *args, **options):
        
        
        for c in ShopCategoryfilters.objects.using('old').all():
            print(c.id)
            category_id = c.category_id
            filter_id = c.filter_id
            category = Category.objects.filter(pk=category_id).first()
            if not category:
                continue
            filter = ShopFilter.objects.using('old').filter(pk=filter_id).first()
            fk = FilterCategory.objects.filter(category=category,name=filter.name).first()
            if not fk:
                fk = FilterCategory(pk=filter.id,category=category,name=filter.name)
                if not filter.slug:
                    slug = slugify(filter.name)
                else:
                    slug = filter.slug
                fk.slug = slug
                fk.save()
            for fs in ShopFilterselect.objects.using('old').filter(filter=filter):
                nfs = FilterSelect.objects.filter(filter_category=fk,name=fs.value).first()
                if not nfs:
                    if not fs.slug:
                        fs_slug = slufify(fs.name)
                    else:
                        fs_slug = fs.slug
                    nfs = FilterSelect(pk=fs.id, filter_category=fk,name=fs.value)
                    nfs.slug = fs_slug
                    nfs.save()

        for fi in ShopFilteritem.objects.using('old').all():

            prod = Product.objects.filter(pk=fi.product_id).first()
            if not prod:
                continue
            
            filter = FilterCategory.objects.filter(pk=fi.filter.id).first()
            if not filter:
                continue
            fs = FilterSelect.objects.filter(filter_category=filter,name=fi.value).first()
            if not fs:
                fs = FilterSelect(filter_category=filter,name=fi.value)
                fs.save()

            fitem = ProductFilter.objects.filter(product=prod,filter_category=filter).first()
            if not fitem:
                fitem = ProductFilter(product=prod,filter_category=filter)
                fitem.save()

            fitem.values.add(fs)
            fitem.save()
            print("SAVE fitem "+str(fitem.id))






            
            
            