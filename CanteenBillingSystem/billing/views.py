from django.shortcuts import render
from .forms import ItemForm,RechargeForm
from .models import Cart,Customer,Item,Product,Recharge
from django.http import HttpResponse,HttpResponseForbidden
import json
# Create your views here.


#client views

def makeOrder(request):
    if request.method=='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            customer = Customer.objects.get(user=request.user)
            balance = customer.balance
            if(balance >= product.price):
                cart = Cart(customer=customer)
                cart.save()
                item = Item(cart=cart,product=product)
                item.save()
                customer.balance-=product.price
                customer.save()
                message = "order placed"
            else:
                message = "insufficient balance!"
    else:
        form = ItemForm()
    return render(request,'shop.html',locals())


def viewOrders(request):
    customer = Customer.objects.get(user=request.user)
    pending_orders = []
    carts = Cart.objects.filter(customer=customer).filter(delivered=False)
    for cart in carts:
        items = Item.objects.filter(cart=cart)
        for item in items:
            pending_orders.append(item.product)
    return render(request,'myorders.html',locals())


def cancelOrder(request):
    customer = Customer.objects.get(user=request.user)
    try:
        carts = Cart.objects.filter(customer=customer).filter(delivered=False).order_by('-date')
        cart = carts[0]
        item = Item.objects.get(cart=cart)
        name = item.product.name
        price = item.product.price
        customer.balance+=price
        customer.save()
        cart.delete()
        message = "your order of {0} was cancelled!".format(name)
    except:
        message = "no orders found!"
    return render(request,'cancelorder.html',locals())



def recharge(request):
    max_tries = 5;
    if request.method=='POST':
        customer = Customer.objects.get(user=request.user)
        form = RechargeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                result = Recharge.objects.get(code=code)
            except:
                result=[]
            try:
                attempts = request.session['times']
            except NameError:
                request.session['times']=0
            if request.session['times']>max_tries-1:
                if customer.reset == True:
                    request.session['times']=0
                    customer.reset=False
                    customer.locked=False
                    customer.save()
                else:
                    customer.locked=True
                    customer.save()
                    message = "ACCOUNT LOCKED!! CONTACT ADMIN"
                    return HttpResponseForbidden()

            if result:
                if result.used == False:
                    message = "recharge done for {0}rs".format(result.worth)
                    customer.balance+=result.worth
                    customer.save()
                    result.used=True
                    result.save()
                else:
                    message = "card already used"
            else:
                request.session['times']+=1
                message = "card doesnt exist!! ({0} tries remaining)".format(max_tries-request.session['times'])
    else:
        form = RechargeForm()
    return render(request,'recharge.html',locals())



#admin views

def todaysList(request):
    carts = Cart.objects.filter(delivered=False)
    pending = {}
    count=0
    for cart in carts:
        customer = cart.customer
        items = Item.objects.filter(cart=cart)
        for item in items:
            try:
                pending[customer.user.username].append(item.product.name)
            except:
                l = [item.product.name]
                count+=item.product.price
                pending[customer.user.username] = l
    data = json.dumps(pending)
    for cart in carts:
        cart.delivered=True
        cart.save()
    return HttpResponse(data)

    #return render(reque
