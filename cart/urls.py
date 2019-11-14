from django.conf.urls import url
from . import views

app_name="cart"

urlpatterns=[
    url(r'^$', views.detail_cart, name='cart_detail'),
    url(r"^add/(?P<product_id>\d+)/$", views.add_cart, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.remove_cart, name='cart_remove'),
]