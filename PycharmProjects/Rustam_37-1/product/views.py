from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product
from product.models import Category
def hello_view(request):
    return HttpResponse("Hello! It's my project")

def current_date_view(request):
    current_date = datetime.now().strftime("%Y-%m-%d")
    return HttpResponse('Current date: '+ current_date)

def goodbye_view(request):
    return HttpResponse("Goodbye user!")


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def product_list_view(request):
    if request.method == 'GET':

        products = Product.objects.all()
        print(products)
        context = {'products': products}

        return render(
            request=request,
            template_name='product/product_list.html',
            context=context
            )



def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)

        context = {'product': product}

        return render(
            request=request,
            template_name='product/product_detail.html',
            context=context
        )


def categories_list_view(request):
    if request.method == 'GET':

        categories = Category.objects.all()
        context = {'categories': categories}

        return render(
            request=request,
            template_name='product/category_list.html',
            context=context
            )