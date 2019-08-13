from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('website_add/',views.website_add,name='website_add'), #访问门户的添加路由
    path('website_edit/',views.website_edit,name='website_edit'), #访问门户的编辑路由
    path('website_info/',views.website_info,name='website_info'), #访问门户的信息路由
    path('website_list/',views.website_list,name='website_list'), #访问门户的列表路由
]
