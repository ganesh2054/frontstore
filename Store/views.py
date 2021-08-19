from django.db.models import Q
from django.db.models.expressions import Value
from django.utils.functional import cached_property
from Store.models import Banner, Collection, Customer, Order, Product, event, orderItem
from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse
from django.db.models.aggregates import Count,Max
from django.views import View

class Index(View):
    def post(self,request):
        product=request.POST.get('product')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                cart[product]=quantity+1
            else:
                cart[product]=1

        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        

        print('our product are',request.session['cart'])
   
        return redirect ('homepage')


    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        cid=request.GET.get('cat')
        banner=Banner.objects.filter(active=True,large=True).first()
        queryset=Banner.objects.filter(active=True,large=False)
        category=Collection.objects.all()
        if cid:
            trending=Product.objects.filter(trending=True,active=True).filter(collection__id=cid)
        else:
            trending=Product.objects.filter(trending=True,active=True).filter()
        hot=Product.objects.filter(hot=True,active=True)
        eventp=event.objects.last()
  
        return render(request,'index.html',{'topbanner':banner,'smallbanner':list(queryset),'category':list(category),'trending':list(trending),'hot':list(hot),'event':eventp})

 
class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        cart_product=Product.get_product_by_id(ids)
        return render(request,'cart.html',{'product':cart_product})


    def post(self,request):
        product=request.POST.get('productc')
        quantity=request.POST.get('')
        cart=request.session.get('cart')







