from django.contrib import admin
from django.urls import path, include
from product import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', product_views.category_list, name='category_list'),
    path('api/v1/categories/<int:id>/', product_views.category_detail, name='category_detail'),
    path('api/v1/products/', product_views.product_list, name='product_list'),
    path('api/v1/products/<int:id>/', product_views.product_detail, name='product_detail'),
    path('api/v1/reviews/', product_views.review_list, name='review_list'),
    path('api/v1/reviews/<int:id>/', product_views.review_detail, name='review_detail'),
    path('api/v1/products/reviews/', product_views.product_reviews, name='product_reviews'),
    path('api/v1/users/', include('users.urls')),
]