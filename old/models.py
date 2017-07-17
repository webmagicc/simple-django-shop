# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ShopBrand(models.Model):
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    metakey = models.CharField(db_column='metaKey', max_length=250)  # Field name made lowercase.
    metadesc = models.CharField(db_column='metaDesc', max_length=250)  # Field name made lowercase.
    slug = models.CharField(unique=True, max_length=250)
    description = models.TextField()
    full_text = models.TextField()
    pub_date = models.DateField()
    published = models.IntegerField()
    ordering = models.IntegerField(blank=True, null=True)
    count_prod = models.IntegerField(blank=True, null=True)
    reit = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    count_votes = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_brand'


class ShopCategory(models.Model):
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    metakey = models.CharField(max_length=250)
    metadesc = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField()
    published = models.IntegerField()
    ordering = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    one = models.CharField(max_length=250)
    name2 = models.CharField(max_length=250)
    low_price = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    ak = models.IntegerField(blank=True, null=True)
    count_prod = models.IntegerField(blank=True, null=True)
    reit = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    count_votes = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    pattern_title = models.CharField(max_length=250)
    pattern_date = models.TextField()
    pattern_key = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'shop_category'


class ShopProduct(models.Model):
    name = models.CharField(max_length=250)
    maincolor = models.CharField(max_length=250, blank=True, null=True)
    idname = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    category = models.ForeignKey(ShopCategory, models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey(ShopBrand, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=250)
    metakey = models.CharField(db_column='metaKey', max_length=250)  # Field name made lowercase.
    metadesc = models.CharField(db_column='metaDesc', max_length=250)  # Field name made lowercase.
    slug = models.CharField(unique=True, max_length=250)
    description = models.TextField()
    full_text = models.TextField()
    pub_date = models.DateField()
    published = models.IntegerField()
    is_new = models.IntegerField()
    ordering = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    oldprice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    count_views = models.IntegerField(blank=True, null=True)
    colors = models.TextField(blank=True, null=True)
    allfilters = models.TextField(blank=True, null=True)
    allproperties = models.TextField(blank=True, null=True)
    reit = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    count_votes = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    recomend = models.IntegerField()
    saleslider = models.IntegerField()
    price_ue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    in_shop = models.IntegerField()
    selling_out = models.IntegerField()
    action = models.IntegerField()
    action_time = models.DateTimeField()
    action_name = models.CharField(max_length=250, blank=True, null=True)
    oldid = models.CharField(max_length=250)
    oldsource = models.CharField(max_length=250)
    price_2 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    discontinued = models.IntegerField()
    slugcolor = models.CharField(max_length=250)
    instruction = models.CharField(max_length=100, blank=True, null=True)
    maincolor_id = models.CharField(max_length=250, blank=True, null=True)
    #action_page = models.ForeignKey('ContentAction', models.DO_NOTHING, blank=True, null=True)
    all_colors = models.TextField(blank=True, null=True)
    instruction_url = models.CharField(max_length=250, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    is_gift = models.IntegerField()
    fil1 = models.CharField(max_length=250)
    fil1_img = models.CharField(max_length=250)
    fil2 = models.CharField(max_length=250)
    fil2_img = models.CharField(max_length=250)
    fil3 = models.CharField(max_length=250)
    fil3_img = models.CharField(max_length=250)
    fil4 = models.CharField(max_length=250)
    fil4_img = models.CharField(max_length=250)
    fil1_val = models.CharField(max_length=250)
    fil2_val = models.CharField(max_length=250)
    fil3_val = models.CharField(max_length=250)
    fil4_val = models.CharField(max_length=250)
    #gift = models.ForeignKey('ShopGift', models.DO_NOTHING, blank=True, null=True)
    need = models.IntegerField()
    search = models.TextField()
    url_hotline = models.CharField(max_length=250)
    full_text2 = models.TextField()
    gen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product'

class ShopCategoryfilters(models.Model):
    category_id = models.IntegerField()
    filter_id = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_categoryfilters'
        


class ShopFilter(models.Model):
    name = models.CharField(max_length=250)
    requery = models.IntegerField()
    show = models.IntegerField()
    filtertype = models.IntegerField()
    slug = models.CharField(max_length=250)
    inlist = models.IntegerField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'shop_filter'


class ShopFilteritem(models.Model):
    product = models.ForeignKey(ShopProduct, models.DO_NOTHING)
    filter = models.ForeignKey(ShopFilter, models.DO_NOTHING)
    value = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'shop_filteritem'


class ShopFilterselect(models.Model):
    filter = models.ForeignKey(ShopFilter, models.DO_NOTHING)
    value = models.CharField(max_length=250)
    ordering = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=250)
    short_value = models.CharField(max_length=250)
    old_slug = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'shop_filterselect'


class ShopProperty(models.Model):
    name = models.CharField(max_length=250)
    ordering = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_property'


class ShopPropertyfilters(models.Model):
    category = models.ForeignKey(ShopCategory, models.DO_NOTHING)
    property = models.ForeignKey(ShopProperty, models.DO_NOTHING)
    ordering = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_propertyfilters'


class ShopPropertyproduct(models.Model):
    value = models.CharField(max_length=250)
    product = models.ForeignKey(ShopProduct, models.DO_NOTHING)
    property = models.ForeignKey(ShopProperty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_propertyproduct'



