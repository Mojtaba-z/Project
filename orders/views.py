from django.shortcuts import render,redirect
from shop.models import Product
from cart.cart import Cart
from .models import Order,OrderItem
from .forms import OrderCreateForm
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from shop.models import Category


@login_required()
def order_create(request):
    categories = Category.objects.all()
    cart=Cart(request)
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
    form = OrderCreateForm(request.POST or None)

    if request.method=='POST':

        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],

                )
            cart.clear()
        return redirect('orders:complete')

    else:
        form=OrderCreateForm()


    return render(request,'index/checkout.html',{'form':form
                                                 ,'cart':cart
                                                 ,'categories':categories,})



def complete(request):
    return render(request,'index/complete.html',{})
