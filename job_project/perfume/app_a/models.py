import self as self
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="products")
    offer = models.CharField(max_length=10)
    price_og = models.CharField(max_length=10)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.title


class Banner(models.Model):
    bnr_btm_one = models.ImageField(upload_to="banner")
    bnr_btm_two = models.ImageField(upload_to="banner")

    def __str__(self):
        return self.bnr_btm_one


class StoreKing(models.Model):
    title_k = models.CharField(max_length=200)
    image_k = models.ImageField(upload_to="store")
    offer_k = models.CharField(max_length=10)
    desc_k = models.TextField()
    price_og_k = models.CharField(max_length=10)
    price_k = models.IntegerField()

    def __str__(self):
        return self.title_k


class StoreQueen(models.Model):
    title_q = models.CharField(max_length=200)
    image_q = models.ImageField(upload_to="store")
    offer_q = models.CharField(max_length=10)
    desc_q = models.TextField()
    price_og_q = models.CharField(max_length=10)
    price_q = models.IntegerField()

    def __str__(self):
        return self.title_q


class Banners(models.Model):
    title_b = models.CharField(max_length=200)
    image_b = models.ImageField(upload_to="banners")
    adv_b = models.TextField()

    def __str__(self):
        return self.title_b


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    translation_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
