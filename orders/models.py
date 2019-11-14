from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name=models.CharField(max_length=150,verbose_name='نام')
    last_name=models.CharField(max_length=150,verbose_name="نام خانوادگی")
    email=models.EmailField(verbose_name="ایمیل")
    phone=models.CharField(max_length=150,verbose_name="شماره موبایل")
    address=models.CharField(max_length=150,verbose_name="آدرس")
    postal_code=models.CharField(max_length=150,verbose_name="کدپستی")
    city=models.CharField(max_length=150,verbose_name="شهر")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False,verbose_name="پرداخت شده")

    class Meta:
        ordering=('-created',)
        verbose_name='سفارشات'
        verbose_name_plural='سفارشات'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all)

    def __str__(self):
        return 'Order{}'.format(self.id)



class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="سقارش")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='قیمت')
    quantity=models.PositiveIntegerField(default=1,verbose_name="تعداد")

    class Meta:
        verbose_name='آیتم سفارش داده شده'
        verbose_name_plural='آیتم های سفارش داده شده'

    def __str__(self):
        return ''.format(self.id)

    def get_total_cost(self):
        return self.price*self.quantity
