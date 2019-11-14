from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=150,verbose_name='نام دسته')
    slug=models.SlugField(max_length=150,verbose_name='لینک')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='ساخته شده در')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='آپدیت شده در ')

    class Meta:
        ordering=('name',)
        verbose_name='دسته'
        verbose_name_plural='دسته ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:list_by_category',args=[self.slug])



class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='انتخاب دسته محصول')
    name=models.CharField(max_length=150 , verbose_name='نام محصول')
    slug=models.SlugField(max_length=150 , verbose_name='لینک')
    description=models.TextField(max_length=2000 , verbose_name='توضیحات محصول')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='قیمت')
    available=models.BooleanField(default=False,verbose_name='موجودی')
    off=models.BooleanField(default=False , verbose_name='تخفیف')
    number=models.PositiveIntegerField(verbose_name='تعداد موجود')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='ProductImage', verbose_name='عکس محصول')

    class Meta:
        ordering=('name',)
        verbose_name="محصول"
        verbose_name_plural='محصولات'
        permissions=[
            ("can_read_private_section","Vip User"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])




class Comment(models.Model):

    post=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='کامنت')

    content=models.TextField(max_length=1600,verbose_name='محتوای کامنت')

    class Meta:
        verbose_name="کامنت"
        verbose_name_plural="کامنت ها"

















