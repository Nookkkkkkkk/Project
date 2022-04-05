from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.index),
    path('register',views.RegisterAccounts),
    path('login', views.login),
    path('logout',login_required(views.logout,login_url='/#login')),
]