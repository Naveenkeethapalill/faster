from django.shortcuts import render , redirect 
from django.http import HttpResponse
from . models import Test
from . forms import TestForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
def index(request):
    return render (request,'index.html')
def about(request):
    return render (request,'about.html')
@login_required
def order(request):
    name=""
    form=TestForm()
    if request.method=='POST':
       form=TestForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect ('index')
    return render (request,'order.html',{'form':form})
@login_required
def myorders(request):
    user = User.objects.get(username=request.user.username)
    test = Test.objects.filter(name=user)
    return render (request,'myorders.html', {'test':test})
def service(request):
    return render (request,'service.html')
def contact(request):
    return render (request,'contact.html')
def login(request):
    return render (request,'login.html')
def create(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm (request.POST)
        if form .is_valid ():
            form.save()
            return redirect ('index')
    return render (request,'create.html',{'form':form})

