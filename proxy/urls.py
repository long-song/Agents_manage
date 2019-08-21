from django.contrib import admin
from django.urls import path, include,re_path
from proxy import views

urlpatterns = [
    path('customer_list/', views.customer_list, name='customer_list'),  # 访问代理商客户管理路由
    path('customer_find/', views.customer_find, name='customer_find'),  # 访问代理商客户管理路由
    path('customer_add/', views.customer_add, name='customer_add'),  # 访问代理商客户添加路由
    path('province/', views.province, name='province'),  # 访问获取省市区信息路由
    path('city/', views.city, name='city'),  # 访问获取省市区信息路由
    path('area/', views.area, name='area'),  # 访问获取省市区信息路由
    path('address/', views.address, name='address'),  # 访问获取省市区信息路由
    path('customer_charge/', views.customer_charge, name='customer_charge'),  # 访问代理商客户充值路由
    path('customer_edit/', views.customer_edit, name='customer_edit'),  # 访问代理商客户编辑路由
    path('customer_info/', views.customer_info, name='customer_info'),  # 访问代理商客户信息路由
    path('customer_del/', views.customer_del, name='customer_del'),  # 访问代理商客户删除路由
    path('customerPay_list/', views.customerPay_list, name='customerPay_list'),  # 访问代理商预付款管理路由
    path('customerPay_find/', views.customerPay_find, name='customerPay_find'),  # 访问代理商预付款管理路由
    path('log_list/', views.log_list, name='log_list'),  # 访问操作日志管理路由
    path('log_list_find/', views.log_list_find, name='log_list_find'),  # 访问操作日志查找路由

]
