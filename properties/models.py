from django.db import models
from django.utils.translation import to_locale, get_language, ugettext_lazy as _

from simple_django_shop.models import (
    BaseModel,
    OrderingBaseModel,
    )
from django.utils.encoding import python_2_unicode_compatible, force_text



class CategoryProperty(OrderingBaseModel):
    name = models.CharField(_("Name"),
        default="",
        max_length=250)
    category = models.ForeignKey('shop.Category',
        on_delete=models.CASCADE,
        related_name='categories_property',
        verbose_name =_('Category'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category property')
        verbose_name_plural = _('Category properties')



class ProductProperty( OrderingBaseModel):
    category_property = models.ForeignKey(CategoryProperty,
        on_delete=models.CASCADE,
        related_name='category_property',
        verbose_name =_('Propery'))
    value = models.CharField(_("Value"),
        default="",
        max_length=250)
    product = models.ForeignKey('shop.Product',
        on_delete=models.CASCADE,
        related_name='properties_product',
        verbose_name =_('Product'))

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = _('Product property')
        verbose_name_plural = _('Product properties')