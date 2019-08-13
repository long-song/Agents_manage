from django.contrib import admin
from django.urls import path, include
from proxy import views

urlpatterns = [
    path('customer_list/', views.customer_list, name='customer_list'),  # 访问代理商客户管理路由
    path('customer_add/', views.customer_add, name='customer_add'),  # 访问代理商客户添加路由
    path('customer_charge/', views.customer_charge, name='customer_charge'),  # 访问代理商客户充值路由
    path('customer_edit/', views.customer_edit, name='customer_edit'),  # 访问代理商客户编辑路由
    path('customer_info/', views.customer_info, name='customer_info'),  # 访问代理商客户信息路由
    path('customerPay_list/', views.customerPay_list, name='customerPay_list'),  # 访问代理商预付款管理路由
    path('log_list/', views.log_list, name='log_list'),  # 访问操作日志管理路由
]
