from django.db.models import Q
from django.db.models.expressions import Value
from Store.models import Collection, Customer, Order, Product, orderItem
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Max

def say_hello(request):
    query_set=Product.objects.all

    return render(request,'hello.html')
