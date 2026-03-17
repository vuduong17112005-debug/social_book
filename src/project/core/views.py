from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post

@login_required(login_url='signin')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')
    return render(request, 'signin.html')

def logout_user(request):
    logout(request)
    return redirect('signin')
def index(request):
    return render(request, 'index.html')
def profile(request):
    # Lấy profile của chính người đang đăng nhập
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            user_profile.profileimg = image
        
        user_profile.bio = request.POST.get('bio')
        user_profile.location = request.POST.get('location')
        user_profile.save()

        return redirect('settings')

    return render(request, 'settings.html', {'user_profile': user_profile})
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST.get('caption')

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/') # Đăng xong quay về trang chủ
    else:
        return redirect('/')
def index(request):
    # Lấy toàn bộ bài viết, cái nào mới nhất thì hiện lên đầu (dùng dấu trừ trước created_at)
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})