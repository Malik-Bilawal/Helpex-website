from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('blog/', views.blog, name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:slug>/', views.gallery_image_detail, name='gallery_detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('why-choose-us/', views.why_choose_us, name='why_choose_us'),
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
]