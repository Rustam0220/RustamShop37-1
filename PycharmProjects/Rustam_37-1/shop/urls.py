
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product.views import  HelloView,CurrentDateView,GoodbyeView,MainView,ProductListView,ProductDetailView,CategoriesListView,CreateReviewView, CreateProductView,CreateCategoryView,ProductUpdateView

from user.views import register_view, login_view, profile_view, logout_view, confirm_view, update_profile_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloView.as_view(), name='hello'),
    path('current_date/', CurrentDateView.as_view(), name='current_date'),
    path('goodbye/', GoodbyeView.as_view(), name='goodbye'),
    path('', MainView.as_view(), name='main'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', CategoriesListView.as_view(), name='category_list'),
    path('create_review/<int:product_id>/', CreateReviewView.as_view(), name='create_review'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),

    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout_view'),
    path('confirm/', confirm_view, name='confirm_view'),
    path('profile/update/', update_profile_view, name='update_profile'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)