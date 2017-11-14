from django.conf.urls import url,include

from .views import makeOrder,viewOrders,cancelOrder,todaysList,recharge

urlpatterns=[
url(r'^order',makeOrder),
url(r'^myorders',viewOrders),
url(r'^cancel',cancelOrder),
url(r'^chef',todaysList),
url(r'^recharge',recharge),


]
