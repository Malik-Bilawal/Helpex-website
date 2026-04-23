from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('blog/', views.blog, name='blog'),
]