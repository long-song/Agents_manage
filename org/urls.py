from django.contrib import admin
from django.urls import path, include
from org import views

urlpatterns = [
    path('role_index/', views.org_role_index, name='org_role_index'),  # 角色首页
    path('<int:o_role>', views.org_role_index, name='org_role_index1'),  # 首页分页
    path('role_find/<int:o_role>', views.role_find, name='role_find'),  # 查询角色
    path('role_add/', views.role_add, name='role_add'),  # 新增角色信息
    path('role_info/<int:info>', views.role_info, name='role_info'),  # 查看角色信息
    path('role_edit/<int:edit>', views.role_edit, name='role_edit'),  # 编辑角色信息
    path('role_grant/', views.role_grant, name='role_grant'),  # 授权角色
    path('role_delete/<int:r_delete>', views.role_delete, name='role_delete'),  # 授权角色

    path('org_menu_index/', views.org_menu_index, name='org_menu_index'),  # 菜单首页
    path('org_menu_index/<int:o_menu>', views.org_menu_index, name='org_menu_index1'),  # 菜单分页
    path('menu_find/<int:m_find>', views.menu_find, name='menu_find'),  # 菜单信息查找
    path('menu_add/', views.menu_add, name='menu_add'),  # 新增菜单信息
    path('menu_info/<int:m_info>', views.menu_info, name='menu_info'),  # 查看菜单信息
    path('menu_edit/<int:m_edit>', views.menu_edit, name='menu_edit'),  # 编辑菜单信息
    path('menu_delete/<int:m_delete>', views.menu_delete, name='menu_delete'),  # 删除菜单信息

    path('org_user_index/', views.org_user_index, name='org_user_index'),  # 用户首页
    path('org_user_index/<int:o_user>', views.org_user_index, name='org_user_index1'),  # 用户分页路由
    path('user_find/<int:u_find>', views.user_find, name='user_find'),  # 查找用户信息
    path('user_add/', views.user_add, name='user_add'),  # 新增用户
    path('user_edit/<int:u_edit>', views.user_edit, name='user_edit'),  # 用户信息修改
    path('user_delete/<int:u_delete>', views.user_delete, name='user_delete'),  # 删除用户
    path('user_off/', views.user_off, name='user_off'),  # 禁用用户
    path('user_pay/', views.user_pay, name='user_pay'),  # 用户预付款

    path('org_finace/', views.org_finace, name='org_finace'),  # 访问系统管理的财务管理路由

    path('keyword_add/', views.keyword_add, name='keyword_add'),  # 关键词申请
    path('keyword_check/', views.keyword_check, name='keyword_check'),  # 关键词申请管理
    path('keyword_list', views.keyword_list, name='keyword_list'),  # 关键词审核
]
