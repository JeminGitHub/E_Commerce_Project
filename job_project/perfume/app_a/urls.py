from django.urls import path

from . import views


urlpatterns = [

    path('',views.index, name='home'),
    path('store/',views.store, name='store'),
    path('storeq/',views.storeq, name='storeq'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateItem,name='update_item'),
    path('studio/', views.studio, name='studio'),
]
