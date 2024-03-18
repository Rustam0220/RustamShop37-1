from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView
from datetime import datetime
from django.db.models import Q
from product.models import Product
from product.models import Category
from product.forms import ProductForm, ReviewForm, CategoryForm, ProductEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello! It's my project")

class CurrentDateView(View):
    def get(self, request):
        current_date = datetime.now().strftime("%Y-%m-%d")
        return HttpResponse('Current date: ' + current_date)

class GoodbyeView(View):
    def get(self, request):
        return HttpResponse("Goodbye user!")

class MainView(View):
    def get(self, request):
        return render(request, 'index.html')

class ProductListView(View):
    def get(self, request):
        search = request.GET.get('search')
        category_id = request.GET.get('category')
        sort = request.GET.get('sort')
        page = request.GET.get('page', 1)

        products = Product.objects.all()
        if search:
            products = products.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        if category_id:
            products = products.filter(categories=category_id)

        if sort == 'rate':
            order = request.GET.get('order')
            if order == 'asc':
                products = products.order_by('rate')
            else:
                products = products.order_by('-rate')
        elif sort == 'created_at':
            order = request.GET.get('order')
            if order == 'asc':
                products = products.order_by('created_at')
            else:
                products = products.order_by('-created_at')

        limit = 5
        max_pages = products.count() / limit
        if max_pages % 1 != 0:
            max_pages = int(max_pages) + 1

        pages = [i for i in range(1, int(max_pages) + 1)]

        start = (int(page) - 1) * limit
        end = start + limit

        products = products[start:end]

        context = {
            'products': products,
            'categories': Category.objects.all(),
            'pages': pages
        }

        return render(
            request=request,
            template_name='product/product_list.html',
            context=context
        )

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ReviewForm()
        context = {'product': product, 'form': form}
        return render(
            request=request,
            template_name='product/product_detail.html',
            context=context
        )

class CategoriesListView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(
            request=request,
            template_name='product/category_list.html',
            context=context
        )

class CreateReviewView(View):
    def post(self, request, product_id):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product_id = product_id
            review.save()
            return redirect('product_detail', product_id=product_id)
        else:
            form = ReviewForm()
        return render(request, 'product/product_detail.html', {'form': form})

class CreateProductView(LoginRequiredMixin, View):
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')


class CreateCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(
            request=request,
            template_name='product/create_category.html',
            context={"form": form}
        )

    def post(self, request):
        form = CategoryForm(request.POST)

        if not form.is_valid():
            return render(
                request=request,
                template_name='product/create_category.html',
                context={"form": form}
            )

        form.save()
        return redirect('/categories/')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'product/update_product.html'
    success_url = '/products/'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)
