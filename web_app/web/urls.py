from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('secret/', views.secret, name='web-secret')
]
