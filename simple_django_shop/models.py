from django.db import models
from django.utils.translation import to_locale, get_language, ugettext_lazy as _


class BaseModel(models.Model):
    """
    Absrtact model
    Add to standart models date of
    crete and update
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'Creation date'))
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_(u'Modification date'))

    objects = models.Manager()

    class Meta:
        abstract = True

class OrderingBaseModel(BaseModel):
    """
    Absrtact model
    Add to BaseModel  published,
    ordering
    """
    published = models.BooleanField(
        _(u'Published'),
        default=True,
        help_text=_('Decides whether entity should be treated as active.'))
    ordering = models.IntegerField(_(u'Ordering'), 
        default=0, 
        blank=True, 
        null=True)

    class Meta:
        abstract = True




