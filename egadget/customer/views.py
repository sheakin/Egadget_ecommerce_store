from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.views import View
from account.models import Product,Cart,Orders
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail

#decorator
def signin_required(fn):
  def inner(request,*args,**kwargs):
    if request.user.is_authenticated:
      return fn(request,*args,**kwargs)
    else:
      messages.info(request,"Please Login First")
      return redirect('log')
  return inner

decorators=[signin_required,never_cache]

# Create your views here.

@method_decorator(decorators,name='dispatch')
class HomeView(TemplateView):
  template_name="home.html"
  
# class ProductView(View):
#   def get(self,request,**kwargs):
#     cat=kwargs.get('cat')
#     print(cat)
#     data=Product.objects.filter(category=cat)
#     print(data)
#     return render(request,"products.html")

@method_decorator(decorators,name='dispatch')
class ProductView(ListView):                #listview used to get all the object from a mode, and the we filter from it wht we needed(customizing)
  template_name="products.html"
  queryset=Product.objects.all()
  context_object_name="data"
  def get_queryset(self) -> QuerySet[Any]:
    qs = super().get_queryset()
    qs=qs.filter(category=self.kwargs.get('cat'))
    return qs
  
@method_decorator(decorators,name='dispatch')
class ProductDetailView(DetailView):    #detailview used to get only one object from a model
  template_name="details.html"
  queryset=Product.objects.all()      
  pk_url_kwarg="pid"                 #  paramtere for getting id is assigned to pk_url_kwargs
  context_object_name="product"      #  passed data to template will be accesed using a key here key name i given product.
  
decorators
def addtoCart(request,*args,**kwargs):
    try:
        user = request.user
        pid = kwargs.get('pid')
        product = Product.objects.get(id=pid)
        try:
          cart = Cart.objects.get(user=user, product=product)
          cart.quantity +=1
          cart.save()
          messages.success(request,"Product Quantity updated")
          return redirect('chome')
        except:
          Cart.objects.create(user=user,product=product)
          messages.success(request,"product added to cart")
          return redirect('chome')
    except:
      messages.error(request,"cart entry failed")
      return redirect('chome')

@method_decorator(decorators,name='dispatch')    
class CartListView(ListView):
  template_name="cartlist.html"
  queryset=Cart.objects.all()
  context_object_name="cart"
  
  def get_queryset(self):
    qs = super().get_queryset()
    qs.filter(user=self.request.user)
    return qs
  
decorators
def removeCart(request,*args,**kwargs):
    try:
      cid=kwargs.get('id')
      cart=Cart.objects.get(id=cid)
      cart.delete()
      messages.success(request,"Cart Item Removed")
      return redirect('clist')
    except:
      messages.error(request,"SomethingWent Wrong")
      return redirect('clist') 
    
@method_decorator(decorators,name='dispatch')   
class CheckoutView(TemplateView):
  template_name="checkout.html"
  
  def post(self,request,*args,**kwargs):
    try:
      cid=kwargs.get('cid')
      cart=Cart.objects.get(id=cid)
      product=cart.product
      user=cart.user
      ph=request.POST.get('phone')
      addr=request.POST.get('address')
      Orders.objects.create(product=product,user=user,phone=ph,address=addr)
      cart.delete()
      messages.success(request,"Order Placed Successfully")
      return redirect('clist')
    except Exception as e:
      print(e)
      messages.error(request,"Something Went Wrong,Order Placing CAncelled")
      return redirect('clist')
    
@method_decorator(decorators,name='dispatch')    
class OrderListView(ListView):
  template_name="orders.html"
  queryset=Orders.objects.all()
  context_object_name="orders"
  
  def get_queryset(self):
    qs= super().get_queryset()
    qs=qs.filter(user=self.request.user)
    return qs
  
decorators
def cancelOrder(request,*args,**kwargs):
  try :
    oid=kwargs.get('oid')
    order=Orders.objects.get(id=oid)
    subject="order cancelling acknowledgement"
    msg=f"Your order for {order.product.title} is successfully cancelled"
    fr_om="sheakin92@gmail.com"
    to_add=[request.user.email]
    send_mail(subject,msg,fr_om,to_add)
    order.delete()
    messages.success(request,'Order Cancelled')
    return redirect('olist')
  except Exception as e:
    messages.error(request,e)
    return redirect('olist')
    