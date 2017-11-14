from django.contrib import admin

# Register your models here.
from .models import Customer,Cart,Item,Product,Recharge

admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(Product)
admin.site.register(Recharge)
