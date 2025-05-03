from django.urls import path
from .views import index, about, contact, catalog, products_view, detail_view, ajax_search_products

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('catalog/', catalog, name='catalog'),
    path('products/', products_view, name='products'),
    path('products/<int:pk>/', detail_view, name='detail'),
    path('search/', ajax_search_products, name='ajax_search_products')
]
