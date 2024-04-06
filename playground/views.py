from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
from django.db.models import Q, F


def say_hello(request):
    
    # Q objects are used to make complex queries with logical operators
    
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) & ~Q(unit_price__lt=20)
    #     )
    
    
    
    # f objects are used to make queries with complex conditions
    
    #queryset = Product.objects.filter(inventory=F('collection__id'))
    
    
    
    # Sorting
    
    # unit_price by ascending order, and -title by descending order
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()      # .reverse() reverses the order of the objects
    
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')
    
    
    
    # limiting results
    
    queryset = Product.objects.all()[5:10]
    
    return render(request, 'hello.html', {'name': 'Ayub', 'products': product})