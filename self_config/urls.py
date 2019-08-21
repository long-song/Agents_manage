from django.contrib import admin
from django.urls import path, include
from self_config import views

urlpatterns = [
    path('', views.login,name='login'),  # 登录路由
    path('logout/', views.logout,name='logout'),  # 登录路由
    path('main/', views.main, name='main'),   # 主页路由
    path('password/', views.password, name='password'),  # 访问当前用户密码修改路由
    path('self_user_edit/', views.self_user_edit, name='self_user_edit'),  # 访问当前用户信息编辑路由
    path('self_user_info/', views.self_user_info, name='self_user_info'),  # 访问当前用户信息路由
    path('self_user_pic/', views.self_user_pic, name='self_user_pic')  # 访问当前用户头像路由
]
