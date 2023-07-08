from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt





# Create your views here.

def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    banners = Banner.objects.all()
    banner = Banners.objects.all()
    context = {
        'products': products,
        'banners': banners,
        'banner': banner,
        'cartItems': cartItems
    }
    return render(request, 'index.html', context)


def store(request):
    products_k = StoreKing.objects.all()
    products_q = StoreQueen.objects.all()
    context = {
        'products_k': products_k,
        'products_q': products_q
    }
    return render(request, 'store.html', context)


def storeq(request):
    products_q = StoreQueen.objects.all()
    context = {

        'products_q': products_q
    }
    return render(request, 'storeq.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)



def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)
    return JsonResponse('Item was added', safe=False)


def studio(request):
    return render(request,'studio.html')