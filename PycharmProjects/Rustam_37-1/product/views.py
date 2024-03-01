from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from product.models import Product
from product.models import Category
from product.forms import ProductForm, ReviewForm, CategoryForm
from django.contrib.auth.decorators import login_required
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

    form = ReviewForm()
    context = {'product': product, 'form': form}

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


def create_review_view(request, post_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product_id = post_id
            review.save()
            return redirect('product_detail', product_id=post_id)
        else:
            form = ReviewForm()
        return render(request, 'product/product_detail.html', {'form': form})

@login_required
def create_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('/products/')
    else:
        form = ProductForm()
    return render(request, 'product/create_product.html', {'form': form})



def create_category_view(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(
            request=request,
            template_name='product/create_category.html',
            context={"form": form}
        )
    elif request.method == 'POST':
        form = CategoryForm(request.POST)

        if not form.is_valid():
            return render(
                request=request,
                template_name='product/create_category.html',
                context={"form": form}
            )

        form.save()
        return redirect('/categories/')
