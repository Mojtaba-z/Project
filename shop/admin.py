from django.contrib import admin
from .models import Category,Product,Comment


def make_off(modeladmin , request , queryset):
    result=queryset.update(off=True)
    if result==1:
        message_bit="1 post was"
    else:
        message_bit='{} posts was'.format(result)

    modeladmin.message_user(request,"{} succesfully marked as off".format(message_bit))


def unmake_off(modeladmin , request , queryset):
    queryset.update(off=False)


make_off.short_description='mark product as off'
unmake_off.short_description='unmark product as off'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','id']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','price','available','off','number','created_at','updated_at']
    list_filter = ['created_at','updated_at','available']
    list_editable = ['available','number','price','off']
    prepopulated_fields = {'slug':('name',)}
    actions = [make_off,unmake_off]
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post',]
    list_filter = ['post',]
    search_fields = ['post',]





