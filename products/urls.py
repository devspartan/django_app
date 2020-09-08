from django.conf.urls import url
from  django.urls import path
from .views import (product_view, product_form_view, dynamic_url_routing)

app_name = "products"
urlpatterns = [
    path('', product_view, name='products'),
    path('<int:id>/', dynamic_url_routing, name='dynamic_routing'),
    path('form/', product_form_view, name='product_form'),
]