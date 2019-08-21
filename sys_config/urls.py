from django.contrib import admin
from django.urls import path, include
from sys_config import views

urlpatterns = [
    path('app_edit/', views.app_edit, name='app_edit'),  # 访问app地址路由

    path('finType_add/', views.finType_add, name='finType_add'),  # 访问财务类型添加路由
    path('finType_edit/', views.finType_edit, name='finType_edit'),  # 访问财务类型编辑路由
    path('finType_info/', views.finType_info, name='finType_info'),  # 访问财务类型信息路由
    path('finType_del/', views.finType_del, name='finType_del'),  # 删除财务类型信息路由
    path('finType_list/', views.finType_list, name='finType_list'),  # 访问财务类型管理路由

    path('sertype_add/', views.sertype_add, name='sertype_add'),  # 访问服务类型添加路由
    path('sertype_edit/', views.sertype_edit, name='sertype_edit'),  # 访问服务类型编辑路由
    path('sertype_info/', views.sertype_info, name='sertype_info'),  # 访问服务类型详情路由
    path('sertype_list/', views.sertype_list, name='sertype_list'),  # 访问服务类型管理路由

    path('service_year/', views.service_year, name='service_year'),  # 访问服务年限管理路由

    path('customerType_edit/', views.customerType_edit, name='customerType_edit'),  # 访问客户类型编辑路由
    path('customerType_add/', views.customerType_add, name='customerType_add'),  # 访问客户类型添加路由
    path('customerType_info/', views.customerType_info, name='customerType_info'),  # 访问客户类型信息路由
    path('customerType_del/', views.customerType_del, name='customerType_del'),  # 删除客户类型信息路由
    path('customerType_list/', views.customerType_list, name='customerType_list'),  # 访问客户类型管理路由

    path('license_edit/', views.license_edit, name='license_edit'),  # 访问证件类型编辑路由
    path('license_add/', views.license_add, name='license_add'),  # 访问证件类型添加路由
    path('license_info/', views.license_info, name='license_info'),  # 访问证件类型信息路由
    path('license_del/', views.license_del, name='license_del'),  # 删除证件类型信息路由
    path('license_list/', views.license_list, name='license_list'),  # 访问证件类型管理路由

    path('discount_edit/', views.discount_edit, name='discount_edit'),  # 访问证件类型编辑路由
    path('discount_add/', views.discount_add, name='discount_add'),  # 访问证件类型添加路由
    path('discount_info/', views.discount_info, name='discount_info'),  # 访问证件类型信息路由
    path('discount_del/', views.discount_del, name='discount_del'),  # 删除证件类型信息路由
    path('discount_list/', views.discount_list, name='discount_list'),  # 访问证件类型管理路由
]
