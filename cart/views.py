from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Product,Category
from .cart import Cart
from .forms import CartAddProductForm


def add_cart(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])

    return redirect('cart:cart_detail')


def remove_cart(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')



def detail_cart(request):
    cart=Cart(request)
    categories=Category.objects.all()
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})

    return render(request,'index/cart.html',{'cart':cart,
                                             'categories':categories})

