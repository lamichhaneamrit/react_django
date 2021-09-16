from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
#This part is for chaning the content from the models as Post title 
def index(request):
    posts=Post.objects.all()
    return render (request, 'login.html', {'posts':posts})

#for login
def login(request):
    if request.method =="POST":
        username=request.POST['username']
        #email=request.POST['email']
        password=request.POST['password']

        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('login.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render('login.html')
    else:
    
        return render(request , 'index.html')
       