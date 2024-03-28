from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.registration, name='register'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('confirm/', views.confirm_user, name='confirm'),
]