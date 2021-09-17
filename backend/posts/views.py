from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
#This part is for chaning the content from the models as Post title 
def index(request):
     posts = Post.objects.all()
     return render (request, 'index.html' ,{'posts': posts}) # See the posts added from the django-admin panel

# for post 
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts}) # content from admin panel
#for login
def login(request):
    if request.method =="POST":
        username=request.POST.get['username']
        #email=request.POST['email']
        password=request.POST.get['password']

        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return render('index.html')
    else:
    
        return render(request , 'login.html')
       