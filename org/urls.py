from django.contrib import admin
from django.urls import path, include
from org import views
from org.views import *
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
    path('user_add/', User_Add.as_view(), name='user_add'),  # 新增用户
    path('user_edit/<int:u_edit>', views.user_edit, name='user_edit'),  # 用户信息修改
    path('user_delete/<int:u_delete>', views.user_delete, name='user_delete'),  # 删除用户
    path('user_off/<int:u_off>', views.user_off, name='user_off'),  # 禁用用户
    path('user_pay/<int:u_pay>', views.user_pay, name='user_pay'),  # 用户预付款
    # path('user_pay/<int:u_pay>', views.user_pay, name='user_pay1'),  # 用户预付款
    path('user_pay_find/<int:u_pay_find>', views.user_pay_find, name='user_pay_find'),  # 用户预付款查找

    path('org_finace/', views.org_finace, name='org_finace'),  # 访问系统管理的财务管理路由

    # 关键词keyword-add界面处理
    path('keyword_add/', views.keyword_add, name='keyword_add'),  # 关键词申请
    path('keyword_add_ajax/', views.keyword_add_ajax, name='keyword_add_ajax'),  # 客户搜索
    path('keyword_word_ajax/', views.keyword_word_ajax, name="keyword_word_ajax"),  # 关键词验证
    path('keyword_price_ajax/', views.keyword_price_ajax, name='keyword_price_ajax'),  # 价格计算

    # 关键词keyword-check界面处理
    path('keyword_check/', views.keyword_check, name='keyword_check'),  # 关键词申请管理
    path('keyword_check/<int:pindex>', views.keyword_check, name='keyword_check_show'),  # 展示分页
    path('keyword_query_check/<int:pindex>', views.keyword_query_check, name='keyword_query_check'),  # 页面关键词查询

    # -edit 处理，关键词申请
    path('keyword_edit/', views.keyword_edit, name='keyword_edit'),  # 编辑
    path('keyword_edit_ajax/', views.keyword_edit_ajax, name='keyword_edit_ajax'),  # 客户存在验证
    path('keyword_key_name_ajax/', views.keyword_key_name_ajax, name='keyword_key_name_ajax'),  # 关键词存在验证
    path('keyword_key_price_ajax/', views.keyword_key_price_ajax, name="keyword_key_price_ajax"),  # 计算价格

    # -kt  处理  ，开通app
    path('keyword_kt/', views.keyword_kt, name='keyword_kt'),  # 开通app
    path('keyword_kt_show/<int:kt>', views.keyword_kt_show, name='keyword_kt_show'),  # 展示关键词信息
    path('keyword_kt_app_ajax/', views.keyword_kt_app_ajax, name='keyword_kt_app_ajax'),  # 判断注册app名不能重复

    # -xf  处理， 续费功能
    path('keyword_xf/', views.keyword_xf, name='keyword_xf'),  # 续费
    path('keyword_xf_show/<int:xf>', views.keyword_xf_show, name='keyword_xf_show'),  # 显示客户关键词信息，以及操作客户
    path('keyword_xf_ajax/', views.keyword_xf_ajax, name='keyword_xf_ajax'),  # ajax获取服务类型，年限计算价格
    # 关键词续费审核
    path('keyword_list/', views.keyword_list, name='keyword_list'),  # 关键词续费审核
    # 分页
    # path('keyword_list_page/', views.keyword_list_page, {'pindex': 1}, name="keyword_list_page"),  # 分页
    path('keyword_list_page_show/',views.keyword_list_page_show,{'pindex': 1},name="keyword_list_page_show"),
    path('keyword_list_pass/<int:bt>',views.keyword_list_pass,name="keyword_list_pass"),
    path('keyword_list_nopass/<int:bt>',views.keyword_list_nopass,name="keyword_list_nopass")
]
