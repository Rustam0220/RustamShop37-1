
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product.views import hello_view, current_date_view, goodbye_view, main_view, product_list_view, \
    product_detail_view, categories_list_view, create_product_view, create_review_view, create_category_view

from user.views import register_view, login_view, profile_view, logout_view, confirm_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view, name='hello'),
    path('current_date/', current_date_view, name='current_date'),
    path('goodbye/', goodbye_view, name='goodbye'),
    path('', main_view,name='main_view'),
    path('products/', product_list_view),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('categories/', categories_list_view, name='categories_list'),
    path('products/create/', create_product_view),
    path('products/<int:post_id>/create_review/', create_review_view, name='create_review'),
    path('categories/create/', create_category_view, name='create_category'),

    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout_view'),
    path('confirm/', confirm_view, name='confirm_view'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)