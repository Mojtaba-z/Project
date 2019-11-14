from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name="shop"

urlpatterns=[
    path('',views.index,name='index'),
    url(r'^(?P<category_slug>\W+)/$',views.index,name='list_by_category'),
    url(r'^product/(?P<pk>\d+)/$',views.ProductDetail,name='product_detail'),
    path('Category/<int:id>/',views.product_by_category,name='product_by_category'),
    path('login/',views.login,name='login'),
    path('register/',views.Register,name='register'),
    path('change-password/',views.change_password,name='change_password'),
    path('base/',views.base,name='base'),
    path('search/',views.search,name='search')



]