from django.contrib import admin
from .models import Profile, Post # Thêm Profile vào đây

# Đăng ký các model để nó hiện lên trang Admin
admin.site.register(Profile) 
admin.site.register(Post)