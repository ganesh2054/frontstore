from Store.models import Product
from django.contrib import admin
from Store.admin import ProductAdmin
from Tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline

class TagInline(GenericTabularInline):
    model=TaggedItem
    autocomplete_fields=['tag']
    extra=0

class CustomProductAdmin(ProductAdmin):

    inlines=[TagInline]

admin.site.unregister(Product)
admin.site.register(Product,CustomProductAdmin)