from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='proxy-home'),
    path('a42df0cb0a99/index.html', views.secret, name='proxy-secret'),
]
