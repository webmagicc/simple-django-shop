from django.contrib import admin
from .models import CategoryProperty, ProductProperty


class ProductPropertyInline(admin.TabularInline):
    model = ProductProperty
    extra = 1
    verbose_name_plural = 'Values'
    suit_classes = 'suit-tab suit-tab-values'


@admin.register(CategoryProperty)
class CategoryPropertyAdmin(admin.ModelAdmin):
    inlines = [ProductPropertyInline,]
    suit_form_tabs = (('general', 'General'), 
        ('values', 'Values'), )
    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
             'name',
             'category',
             'published',
             'ordering',
             ]
        }),
    ]


@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    pass
