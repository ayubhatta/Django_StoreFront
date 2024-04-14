from django.forms import DecimalField
from django.shortcuts import render
from store.models import Customer, Product, OrderItem
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat

# def say_hello(request):
    
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
    
    # queryset = Product.objects.only('id', 'title')
    # result = Product.objects.filter(collection__id = 1).aggregate(count =  Count('id'), 
    #                                    min_price = Min('unit_price'), 
    #                                    max_price = Max('unit_price'), 
    #                                    avg_price = Avg('unit_price'), 
    #                                    total_price = Sum('unit_price'))
      
      
def say_hello(request):
    
    queryset = Product.objects.order_by('unit_price', '-title').reverse() 
    
    return render(request, 'hello.html', {'name': 'Ayub', 'result': queryset})
