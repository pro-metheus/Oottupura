from .models import Customer,Item,Cart,Product,Recharge
from django import forms
from django.forms import ModelForm


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['product']



class RechargeForm(ModelForm):
    class Meta:
        model = Recharge
        fields=['code']
