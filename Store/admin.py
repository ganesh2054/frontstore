from django.contrib import admin
from django.contrib.admin.decorators import action, display
from django.core.checks.messages import Error
from django.db import models
from django.db.models import Value
from django.db.models.aggregates import Count
from django.utils.html import format_html,urlencode
from django.urls import reverse
from django.utils.html import mark_safe
from .models import Product

from .import models

class InventoryFilter(admin.SimpleListFilter):
    title='inventory'
    parameter_name='inventory'
    
    def lookups(self, request,model_admin):
        return [
            ('<10','Low')
        ]
    def queryset(self, request,queryset):
        if self.value()=='<10':
            return queryset.filter(inventory__lt=10)
        

# class ImageInline(admin.TabularInline):
#   model = models.Photo
#   autocomplete_fields=['product']
#   max_num=10
#   extra=0
  

##Product
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  #  fields=['title','slug']

  #  exclude=['promotions']
    prepopulated_fields={
        'slug':['title']
    }
    autocomplete_fields=['collection']

   # readonly_fields=['title']
    search_fields=['title']
    # inlines=[ImageInline]
 
    action=['clear_inventory']
    list_display=['title','unit_price','description','last_update','slug','inventory','inventory_status','hot','trending','active','collection_title','product_thumnail']
    list_editable=['unit_price']
    list_filter=['collection','last_update',InventoryFilter]
    list_per_page=10
    list_select_related=['collection']

    def product_thumnail(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.product_image.url,
            width='250',
            height='200',
            )
    )

    
    # def queryset(self, request):
    #         return queryset.filter(photo_title=Product.objects.all()[:1].get())


   # readonly_fields = ['product_image']

    # @admin.display(ordering='product_image')
    # def product_image(self,product):
    #     url=(reverse('admin:Store_product_changelist')
    #     +'?'
    #     +urlencode({
    #         'product__id':str(product.id)
    #     }))
    #     return format_html('<a href="{}">{}</a>',url,product.product_image)
    # def get_queryset(self, request):
    #     return super().get_queryset(Product.objects.all()[:1].get())




   # @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if int(product.inventory)<10:
            return 'low'
        return 'ok'
    def collection_title(self,product):
        return product.collection.title

    @admin.action(description='Clear inventory')
    def clear_inventory(self,request,queryset):
        updated_count=queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated'
      
        )
#Customer
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phon','last_update','membership','customer_order']
    list_editable=['membership']
    list_per_page=10
    search_fields=['first_name__istartswith']


    @admin.display(ordering='customer_order')
    def customer_order(self,customer):
        url=(reverse('admin:Store_order_changelist')
        +'?'
        +urlencode({
            'customer__id':str(customer.id)
        }))
        return format_html('<a href="{}">{}</a>',url,customer.customer_order)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(customer_order=Count('order'))


class OrderItemInline(admin.TabularInline):
    model=models.orderItem
    autocomplete_fields=['product']
    min_num=1
    max_num=10
    extra=0

##order
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields=['customer']
    list_display=['placed_at','payment_status','customer_name']
    list_per_page=10
    list_editable=['payment_status']
    list_select_related=['customer']
    inlines=[OrderItemInline]

    def customer_name(self,order):
        return order.customer.first_name


##Collection
 
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','product_count']
    search_fields=['title']

    @admin.display(ordering='product_count')
    def product_count(self,collection):
        url=(reverse(
            'admin:Store_product_changelist')
            +'?'
            +urlencode({
                'collection__id':str(collection.id)
            }))
        return  format_html('<a href="{}">{}</a>',url,collection.product_count)
   

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count('product'))
##Banner

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':['title']
    }
    list_display=['title','slug','product_thumnail']
    readonly_fields = ['product_thumnail']

    def product_thumnail(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width='150',
            height='100',
            )
    )

@admin.register(models.event)
class EventAdmin(admin.ModelAdmin):
    list_display=['title','description','price','discount_price','date','event_thumnail']
    def event_thumnail(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width='150',
            height='100',
            )
    )

    


