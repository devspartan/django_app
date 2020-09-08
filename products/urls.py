from django.conf.urls import url

from .views import (product_view, product_form_view, dynamic_url_routing)

app_name = "products"
urlpatterns = [

    url('p/', product_view, name='product'),
    url('(?P<id>\d+)/', dynamic_url_routing, name='dynamic_routing'),
    url('form/', product_form_view, name='product_form'),

]