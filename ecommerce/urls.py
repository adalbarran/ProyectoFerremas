from django.urls import path
from . import views

urlpatterns = [
    path('ecommerce', views.index, name='ecommerce'),
    path('', views.index, name='index'),

]