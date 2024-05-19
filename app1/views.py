from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def Home(request):
    return render(request,'home.html')
def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse('pass1 and pass2 are not same')
        else:    
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')
def Login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse('incorrect username and password')    

    return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login')