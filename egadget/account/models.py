from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
  title=models.CharField(max_length=100)
  price=models.IntegerField()
  description=models.CharField(max_length=100)
  image=models.ImageField("product_images")
  options=(
    ("Smart phone","Smart phone"),
    ("Tablets","Tablets"),
    ("Smart Watch","Smart Watch"),
    ("Laptop","Laptop")
  )
  category=models.CharField(max_length=200,choices=options)
  def __str__(self):
    return self.title
  
class Cart(models.Model):
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  date=models.DateField(auto_now=True)
  quantity=models.IntegerField(default=1)
  status=models.CharField(max_length=100)
  
  def total_price(self):
    tamount=self.product.price*self.quantity
    return tamount
  
class Orders(models.Model):
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  phone=models.IntegerField()
  address=models.CharField(max_length=500)
  date=models.DateField(auto_now=True)
  options=(
    ("Order Placed","Order Placed"),
    ("Shipped","Shipped"),
    ("Out For Delivery","Out For Delivery"),
    ("Delivered","Delivered")
  )
  status=models.CharField(max_length=100,default="Order Placed",choices=options)