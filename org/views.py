from django.shortcuts import render, HttpResponse
from .models import *
from proxy.models import User
from django.core.paginator import Paginator


# Create your views here.
def org_role_index(request, o_role=1):
    """
    角色首页
    :param request:
    :return:
    """
    role_all = Role.objects.all()
    paginator = Paginator(role_all, 5)  # 分页
    if o_role == '':
        o_role = 1
    else:
        o_role = int(o_role)
    page = paginator.page(o_role)
    return render(request, 'pages/org/role/role-list.html', {'role_all': page, 'count': paginator})


def role_find(request, o_role):
    """
    角色查找
    :param request:
    :return:
    """
    if request.method == 'GET':
        # org_role_index(request)
        pass
        # role_all = Role.objects.all()
        # return render(request, 'org/role/role-list.html', {'role_all': role_all})
    else:
        textfield = request.POST.get('textfield')  # 获取角色名称
        option_state = request.POST.get('option_state')  # 获取权限
        role_all = Role.objects.filter(role_name__icontains=textfield, role_state__exact=option_state)
        print(textfield, option_state)
        paginator = Paginator(role_all, 5)  # 5个分页
        if o_role == '':
            o_role = 1
        else:
            o_role = int(o_role)
        page = paginator.page(o_role)
        return render(request, 'pages/org/role/role-list.html', {'role_all': page})


def role_add(request):
    """
    新增角色
    :param request:
    :return:
    """
    return render(request, 'pages/org/role/role-add.html')



def role_info(request, info):
    """
    查看角色信息
    :param request:
    :return:
    """
    role_info = Role.objects.get(role_id=info)  # 获取单角色信息
    return render(request, 'pages/org/role/role-info.html', {'role_info': role_info})


def role_edit(request, edit):
    """
    编辑角色信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        role_edit = Role.objects.get(role_id=edit)  # 获取单角色信息
        return render(request, 'pages/org/role/role-edit.html', {'role_edit': role_edit})

    else:
        role_edit = Role.objects.get(role_id=edit)  # 获取单角色信息
        text = request.POST.get('text')  # 获取角色名称
        status = request.POST.get('status')
        remark = request.POST.get('remark')
        role_edit.role_name = text
        role_edit.role_state = status
        role_edit.role_remark = remark
        role_edit.save()
        print(edit, text, status, remark)
        # Role.objects.create(role_id=edit, role_name=text, role_state=status, role_remark=remark, role_isdel=1)
        return render(request, 'pages/org/role/role-edit.html', {'role_edit': role_edit})


def role_grant(request):
    """
    授权角色信息
    :param request:
    :return:
    """
    return render(request, 'pages/org/role/role-grant.html')


def role_delete(request):
    """
    删除角色
    :param request:
    :return:
    """
    return HttpResponse('删除成功')


def org_menu_index(request, o_menu=1):
    """
    菜单首页
    :param request:
    :return:
    """
    menu_all = Menu.objects.all()  # 全部菜单信息
    paginator = Paginator(menu_all, 5)  # 分页  5条信息
    if o_menu == '':
        o_menu = 1
    else:
        o_menu = int(o_menu)
    page = paginator.page(o_menu)
    return render(request, 'pages/org/menu/menu-list.html', {'menu_all': page, 'count': paginator})


def menu_find(request):
    """
    菜单信息查找
    :param request:
    :return:
    """
    return HttpResponse('find')


def menu_add(request):
    """
    新增菜单信息
    :param request:
    :return:
    """
    return render(request, 'pages/org/menu/menu-add.html')


def menu_info(request):
    """
    查看菜单信息
    :param reuqest:
    :return:
    """
    return render(request, 'pages/org/menu/menu-info.html')


def menu_edit(request):
    """
    编辑菜单信息
    :param request:
    :return:
    """
    return render(request, 'pages/org/menu/menu-edit.html')


def menu_delete(request):
    """
    删除菜单信息
    :param request:
    :return:
    """
    return HttpResponse('删除成功')


def org_user_index(request, o_user=1):
    """
    用户首页
    :param request:
    :return:
    """
    user_all = User.objects.all()
    paginator = Paginator(user_all, 5)  # 分页  5条信息
    if o_user == '':
        o_user = 1
    else:
        o_user = int(o_user)
    page = paginator.page(o_user)
    return render(request, 'pages/org/user/user-list.html', {'user_all': page, 'count': paginator})


def user_add(request):
    """
    新增用户
    :param request:
    :return:
    """
    return render(request, 'pages/org/user/user-add.html')


def user_edit(request):
    """
    用户信息修改
    :param request:
    :return:
    """
    return render(request, 'pages/org/user/user-edit.html')


def user_delete(request):
    """
    删除用户
    :param request:
    :return:
    """
    return HttpResponse('成功')


def user_off(request):
    """
    禁用用户
    :param request:
    :return:
    """
    return HttpResponse('禁用成功')


def user_pay(request):
    """
    用户预付款
    :param request:
    :return:
    """
    return render(request, 'pages/org/user/user-pay.html')


def org_finace(request):
    """
    访问系统管理的财务管理添加功能
    :param request:
    :return:
    """

    return render(request, 'pages/org/finace/finace-add.html')


def keyword_add(request):
    '''
    关键词申请
    :param request:
    :return:
    '''
    # if request.method == 'GET':
    return render(request, 'pages/org/keyword/keyword-add.html')
    # else:
    #     sourch = request.POST.get('sourch')
    #     name = request.POST.get('name')
    #     keyword = request.POST.get('keyword')
    #     service = request.POST.get('service')
    #     service_year = request.POST.get('service_year')
    #     price = request.POST.get('price')
        # print(sourch,name,keyword,service,service_year,price)


def keyword_check(request):
    '''
    关键词申请管理
    :param request:
    :return:
    '''
    return render(request, 'pages/org/keyword/keyword-check.html')


def keyword_list(request):
    '''
    关键词审核
    :param request:
    :return:
    '''
    return render(request, 'pages/org/keyword/keyword-list.html')

