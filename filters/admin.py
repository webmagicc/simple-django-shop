from django.contrib import admin
from .models import FilterCategory, FilterSelect



class FilterSelectInline(admin.TabularInline):
    model = FilterSelect
    extra = 1
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }



@admin.register(FilterCategory)
class FilterCategoryAdmin(admin.ModelAdmin):
    inlines = [FilterSelectInline,]
    
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }


@admin.register(FilterSelect)
class FilterSelectAdmin(admin.ModelAdmin):
    
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
