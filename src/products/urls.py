from unicodedata import name
from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListview.as_view(), name='index'),
    path('search', views.ProductSearchView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product' ),
    
]