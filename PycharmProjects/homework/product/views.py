from django.shortcuts import render

from product.models import Product


def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {'product': products}
        return render(request, 'product/products.html', context=context)

def product_detail(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product/product_detail.html', context=context)