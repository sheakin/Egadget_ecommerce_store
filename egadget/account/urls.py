from django.urls import path
from .views import *


urlpatterns=[
  path('login/',LoginView.as_view(),name='log'),
  path('reg/',RegView.as_view(),name='reg'),
  path('logout',LogOutView.as_view(),name='lgout')
]