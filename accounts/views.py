from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from accounts.models import Accounts
from .forms import LoginForm, RegistersForm
from django.contrib.auth import login, logout


# Create your views here.
def RegisterAccounts(request):
    form = RegistersForm(request.POST or None)
    if  form.is_valid():
        form.save()
        form = RegistersForm()
    context = {  
                'form' :form,           
    }
    return render(request,'register.html',context)


def index(request):
    return render(request,'login.html')

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    #login เช็ค user กับ pass
    userlogin=auth.authenticate(username=username,password=password) 
    if userlogin is not None :
        auth.login(request,userlogin)
        return redirect('/home')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/')  
def logout(request):
    auth.logout(request)
    return redirect('/')
