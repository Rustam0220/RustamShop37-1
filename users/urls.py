from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.Registration.as_view(), name='register'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('confirm/', views.ConfirmUser.as_view(), name='confirm'),
]