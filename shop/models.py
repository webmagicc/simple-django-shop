from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from django.utils.translation import to_locale, get_language, ugettext_lazy as _
import uuid
from simple_django_shop.models import (
    BaseModel,
    OrderingBaseModel,
    )
from django.utils.encoding import python_2_unicode_compatible, force_text
from properties.models import ProductProperty, CategoryProperty
from filters.models import ProductFilter, FilterCategory
from easy_thumbnails.files import get_thumbnailer
from slugify import slugify


def make_upload_path(instance, filename, prefix = False):
    """
    Create unique name for image or file.
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    f = parts[-1]
    filename = new_name + '.' + f
    return u"%s/%s" % (settings.SHOP_IMAGE_DIR, filename)








class Category(MPTTModel, OrderingBaseModel):
    """
    Category of products
    extend ItemBaseModel
    which has slug, name,
    description, keywords
    """
    slug = models.CharField(_("Slug"),
            default="",
            unique=True,
            max_length=250)
    name = models.CharField(_("Name"),
        default="",
        max_length=250)
    url = models.CharField(_("Scrapy Url"),
            default="",
            blank=True,
            max_length=250)
    title = models.CharField(_("Title"),
        blank=True,
        default="",
        max_length=250)
    description = models.CharField(_("Description"),
        blank=True,
        default="",
        max_length=250)
    keywords = models.CharField(_("Keywords"),
        blank=True,
        default="",
        max_length=250)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name=_('Parent'))
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name=_('Image'))

    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ['name']





class Product(OrderingBaseModel):
    slug = models.CharField(_("Slug"),
            default="",
            blank=True,
            db_index=True,
            max_length=250)
    url = models.CharField(_("Url"),
            default="",
            blank=True,
            max_length=250)
    name = models.CharField(_("Name"),
        default="",
        max_length=250)
    sky = models.CharField(_("Sky"),
        blank=True,
        default="",
        db_index=True,
        max_length=250)
    title = models.CharField(_("Title"),
        blank=True,
        default="",
        max_length=250)
    description = models.CharField(_("Description"),
        blank=True,
        default="",
        max_length=250)
    keywords = models.CharField(_("Keywords"),
        blank=True,
        default="",
        max_length=250)
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name =_('Image'))
    category = models.ForeignKey(Category,
        on_delete=models.CASCADE,
        related_name='categories',
        blank=True,
        null=True,
        verbose_name =_('Category'))
    price = models.DecimalField(max_digits=8,
        decimal_places=2,
        null=True,
        default=0.00,
        verbose_name =_('Price'))
    promo = models.BooleanField(
        _(u'Published'),
        default=False,
        help_text=_('Show this product on Home page?'))

    def get_filters(self):
        res = {}
        category = self.category
        for fp in ProductFilter.objects.filter(product=self):
            name = fp.filter_category.name
            if not fp.filter_category.slug:
                fp.filter_category.slug = slugify(name)
                fp.filter_category.save()
            slug = fp.filter_category.slug
            selects = []
            for s in fp.values.all():
                selects.append(s.name)
            res.update({slug:selects})
        return res
            


    

    def pic(self):
        if self.image:
            thumb_url = get_thumbnailer(self.image)['thumb'].url
            return u'<img src="%s" width="70"/>' % thumb_url
        else:
            return '(none)'
    pic.short_description = u'Большая картинка'
    pic.allow_tags = True
    def save(self, *args, **kwargs):
        if self.category:
            super(Product, self).save(*args, **kwargs)
            # we create properties if not exist
            for cp in CategoryProperty.objects.filter(category=self.category):
                pp = ProductProperty.objects.filter(category_property=cp,
                    product=self)
                if not pp:
                    pp = ProductProperty(category_property=cp, product=self, value="--")
                    pp.save()
            # we create filters if not exist
            for fc in FilterCategory.objects.filter(category=self.category):
                pf = ProductFilter.objects.filter(filter_category=fc,
                    product=self)
                if not pf:
                    pf = ProductFilter(filter_category=fc, product=self)
                    pf.save()



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Offer(OrderingBaseModel):
    product = models.ForeignKey(Product,
        on_delete=models.CASCADE,
        related_name='offers',
        null=True,
        verbose_name =_('Product'))
    name = models.CharField(_("Name"),
        default="",
        max_length=250)
    price = models.DecimalField(max_digits=8,
        decimal_places=2,
        null=True,
        default=0.00,
        verbose_name =_('Price'))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')


class Images( OrderingBaseModel):
    product = models.ForeignKey(Product,
        on_delete=models.CASCADE,
        related_name='images',
        null=True,
        verbose_name =_('Product'))
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name=_('Image'))

    name = models.CharField(_("Name"),
        default="",
        max_length=250)
    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
