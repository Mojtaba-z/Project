from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from .models import Product,Category
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.contrib.auth.decorators import permission_required
from .forms import CommentForm
from .models import Comment
from django.db.models import Q




# using permission for whole of a page
# @permission_required('can_read_private_section')
def index(reuqest,category_slug=None):

    cart=Cart(reuqest)

    OffProducts=Product.objects.filter(off=True)[:10]

    Shampoo=Product.objects.filter(category__id__exact=11)

    Teeth=Product.objects.filter(category__id__exact=10)

    Janebi=Product.objects.filter(category__id__exact=12)

    NewProducts=Product.objects.order_by('-created_at')[:5]

    KharObar=Product.objects.filter(category__id__exact=6)[:10]

    category=None

    categories=Category.objects.all()

    Products=Product.objects.filter(available=True)

    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        Products=Product.objects.filter(category=category)




    context={
        'OffProducts':OffProducts,
        'Shampoo':Shampoo,
        'Teeth':Teeth,
        'Janebi':Janebi,
        'NewProducts':NewProducts,
        'KharObar':KharObar,
        'category':category,
        'categories':categories,
        'Products':Products,
        'cart':cart
    }

    return render(reuqest,'index/index.html',context)


def ProductDetail(request,pk):

    product=get_object_or_404(Product,pk=pk,available=True)

    cart_add_product=CartAddProductForm()

    offproducts=Product.objects.filter(off=True)

    categories=Category.objects.all()

    cart=Cart(request)

    lastproducts=Product.objects.order_by('-created_at')[:10]

    comments=Comment.objects.filter(post=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=product, content=content)
            comment.save()

    else:
        form = CommentForm()

    context={
        'product':product,
        'cart_add_product':cart_add_product,
        'offproducts':offproducts,
        'categories':categories,
        'cart':cart,
        'lastproducts':lastproducts,
        'comments':comments,
        'form':form,
        'user':request.user

    }

    return render(request,'index/product.html',context)




def product_by_category(request,id):
    cart=Cart(request)
    category=get_object_or_404(Category,id=id)
    categories=Category.objects.all()
    product=Product.objects.filter(category=category)
    paginator=Paginator(product,4)
    page=request.GET.get('page')
    product=paginator.get_page(page)
    product2=Product.objects.order_by('-created_at')[:5]

    context={
        'product': product,
        'category':category,
        'categories':categories,
        'product':product,
        'cart':cart,
        'product2':product2,

    }

    return render(request, 'category.html', context)


def login(request):
    categories=Category.objects.all()
    cart=Cart(request)
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            return redirect('shop:index')
    else:
        form=AuthenticationForm()

    return render(request, 'registration/login.html', {'form':form,
                                                       'categories':categories,
                                                       'cart':cart})



def Register(request):
    categories=Category.objects.all()
    cart=Cart(request)
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:index')

    else:
        form=RegistrationForm()

    return render(request,'index/register.html',{'form':form,
                                                 'categories':categories,
                                                 'cart':cart})

def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)

        return redirect('shop:login')

    else:
        form=PasswordChangeForm(user=request.user)

    return render(request,'change_password.html',{'form':form})


def base(request):
    cart=Cart(request)
    categories=Category.objects.all()

    context={
        'categories':categories,
        'cart':cart,
    }

    return render(request, 'index.html',context)



def search(request):

    query=request.GET.get('q')
    if query:
        result=Product.objects.filter(Q(name__icontains=query))
    else:
        result=Product.objects.filter(available=True)

        s=Product.objects.filter(result)

    context={
        'items':s,

    }

    return render(request,'search.html',context)




