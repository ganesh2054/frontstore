from django.db.models import Q
from django.db.models.expressions import Value
from Store.models import Banner, Collection, Customer, Order, Product, event, orderItem
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Max

def say_hello(request):
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


