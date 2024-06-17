from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LogForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,FormView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

class LandingView(TemplateView):
  template_name="index.html"
  # def get(self,request):
  #   return render(request,'index.html')
  
  
class LoginView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
      form_data=LogForm(data=request.POST)
      if form_data.is_valid():
          uname=form_data.cleaned_data.get('username')
          pswd=form_data.cleaned_data.get('password')
          user=authenticate(request,username=uname,password=pswd)
          if user:
              print(user)
              login(request,user)                               #used to take login user name to display in home.
              messages.success(request,"Login succcessfull")
              return redirect('chome')
          else: 
              messages.error(request,"Invalid Username/password")
              return redirect('log')
      return render(request,'log.html',{"form":form_data})
        
    
  
# class RegView(View):
#   form_class=RegisterForm
#   template_name="reg.html"
#   success_url="log"
  # def get(self,request):
  #   form=self.form_class()                                            { we can write this in 3 lines using CreateView and reverse_lazy }
  #   return render(request,self.template_name,{"form":form})
  # def post(self,request):
  #   form_data=self.form_class(data=request.POST)
  #   if form_data.is_valid():
  #     form_data.save()
  #     return redirect(self.success_url)
  #   return render(request,self.template_name,{"form":form_data})
  

class RegView(CreateView):
  form_class=RegisterForm
  template_name="reg.html"
  success_url=reverse_lazy("log")
  def form_valid(self, form: BaseModelForm):
      messages.success(self.request,"Registration Completed")
      return super().form_valid(form)
  def form_invalid(self, form: BaseModelForm):
      messages.error(self.request,"Registration Failed")
      return super().form_invalid(form)
  
class LogOutView(View):
    def get(self,request):
      logout(request)
      return redirect ('landing')