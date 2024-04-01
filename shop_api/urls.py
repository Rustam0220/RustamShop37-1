from django.contrib import admin
from django.urls import path, include
from product import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', product_views.CategoryList.as_view(), name='category_list'),
    path('api/v1/categories/<int:id>/', product_views.CategoryDetail.as_view(), name='category_detail'),
    path('api/v1/products/', product_views.ProductList.as_view(), name='product_list'),
    path('api/v1/products/<int:id>/', product_views.ProductDetail.as_view(), name='product_detail'),
    path('api/v1/reviews/', product_views.ReviewList.as_view(), name='review_list'),
    path('api/v1/reviews/<int:id>/', product_views.ReviewDetail.as_view(), name='review_detail'),
    path('api/v1/products/reviews/', product_views.ProductReviews.as_view(), name='product_reviews'),
    path('api/v1/users/', include('users.urls')),
]