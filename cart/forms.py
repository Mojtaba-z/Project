from django import forms
from shop.models import Product

Quantity_Choices=[(item,str(item)) for item in range(1,20)]

class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=Quantity_Choices,coerce=int)
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)