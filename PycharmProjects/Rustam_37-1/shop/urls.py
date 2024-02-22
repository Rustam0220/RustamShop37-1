
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product.views import hello_view, current_date_view, goodbye_view, main_view, product_list_view, \
    product_detail_view, categories_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view, name='hello'),
    path('current_date/', current_date_view, name='current_date'),
    path('goodbye/', goodbye_view, name='goodbye'),
    path('', main_view),
    path('products/', product_list_view),
    path('products/<int:product_id>/', product_detail_view),
    path('categories/', categories_list_view, name='categories_list')
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)