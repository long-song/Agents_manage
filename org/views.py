from django.shortcuts import render, HttpResponse, redirect
from .models import *
from proxy.models import User
from django.core.paginator import Paginator


# Create your views here.


def org_role_index(request, o_role=1, textfield23=1):
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
    textfield23 = request.POST.get('textfield23')
    print(paginator.page_range)  # 返回分页列表
    num = paginator.page_range
    # for i in num:
    #     if textfield23 == i:
    #         print(i)
    return render(request, 'pages/org/role/role-list.html',
                  {'role_all': page, 'count': paginator, })
    # elif textfield23 ==1:
    #     return render(request, 'org/role/role-list.html',
    #                   {'role_all': page, 'count': paginator, 'textfield23': 1})


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
        # role_all = Role.objects.filter(role_name__contains=textfield, role_state__exact=option_state)
        role_all = Role.objects.filter(role_name__contains=textfield, role_state__exact=option_state)
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
    if request.method == "GET":
        return render(request, 'pages/org/role/role-add.html')

    else:
        role_name = request.POST.get('role_name')  # 获取角色名称
        status = request.POST.get('status')  # 获取角色状态
        role_remark = request.POST.get('role_remark')  # 获取角色备注
        print(role_name, status, role_remark)


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


def role_delete(request, r_delete):
    """
    删除角色
    :param request:
    :return:
    """
    Role.objects.filter(role_id=r_delete).delete()
    # return render(request, 'pages/org/role/role-list.html')
    return redirect('/org/role_index/')


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
    # me_id = Menu.objects.get(menu_id=o_menu)
    return render(request, 'pages/org/menu/menu-list.html', {'menu_all': page, 'count': paginator})


def menu_find(request, m_find):
    """
    菜单信息查找
    :param request:
    :return:
    """
    if request.method == 'GET':
        org_menu_index(request)
    else:
        textfield = request.POST.get('textfield')  # 获取菜单名称
        menu_all = Menu.objects.filter(menu_name__contains=textfield)
        print(menu_all)
        paginator = Paginator(menu_all, 5)  # 5个分页
        if m_find == '':
            m_find = 1
        else:
            m_find = int(m_find)
        page = paginator.page(m_find)
        return render(request, 'pages/org/menu/menu-list.html', {'menu_all': page, 'count': paginator})


def menu_add(request):
    """
    新增菜单信息
    :param request:
    :return:
    """
    return render(request, 'pages/org/menu/menu-add.html')


def menu_info(request, m_info):
    """
    查看菜单信息
    :param request:
    :return:
    """
    menu_one = Menu.objects.get(menu_id=m_info)  # 单菜单详情
    return render(request, 'pages/org/menu/menu-info.html', {'menu_one': menu_one})


def menu_edit(request, m_edit):
    """
    编辑菜单信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        menu_one = Menu.objects.get(menu_id=m_edit)  # 单菜单详情
        return render(request, 'pages/org/menu/menu-edit.html', {'menu_one': menu_one})
    else:
        menu_name = request.POST.get('menu_name')  # 获取菜单名称
        select_menu = request.POST.get('select_menu')  # 获取上级菜单
        menu_state = request.POST.get('menu_state')  # 获取菜单状态
        menu_url = request.POST.get('menu_url')  # 获取菜单网址
        menu_intro = request.POST.get('menu_intro')  # 获取菜单简介
        print(menu_name, select_menu, menu_state, menu_url, menu_intro)
        menu_one = Menu.objects.get(menu_id=m_edit)  # 单菜单详情
        menu_one.menu_name = menu_name
        menu_one.select_menu = select_menu
        menu_one.menu_state = menu_state
        menu_one.menu_url = menu_url
        menu_one.menu_intro = menu_intro
        menu_one.save()
        return render(request, 'pages/org/menu/menu-edit.html', {'menu_one': menu_one})


def menu_delete(request, m_delete):
    """
    删除菜单信息
    :param request:
    :return:
    """
    Menu.objects.filter(menu_id=m_delete).delete()  # 删除选中菜单
    return redirect('/org/org_menu_index')


def org_user_index(request, o_user=1):
    """
    用户首页
    :param request:
    :return:
    """
    user_role = UserRole.objects.all()  # 获取
    paginator = Paginator(user_role, 5)  # 分页  5条信息
    if o_user == '':
        o_user = 1
    else:
        o_user = int(o_user)
    page = paginator.page(o_user)
    return render(request, 'pages/org/user/user-list.html', {'user_role': page, 'count': paginator})


def user_find(request, u_find):
    """
    查找用户
    :param request:
    :return:
    """
    if request.method == 'GET':
        org_user_index(request)
    else:
        textfield = request.POST.get('textfield')  # 获取到用户名称
        user_state = request.POST.get('user_state')  # 获取用户权限
        user_find = UserRole.objects.filter(user__user_realname__contains=textfield, user__user_state__exact=user_state)
        paginator = Paginator(user_find, 5)  # 分页  5条信息
        if u_find == '':
            u_find = 1
        else:
            u_find = int(u_find)
        page = paginator.page(u_find)
        return render(request, 'pages/org/user/user-list.html', {'user_role': page, 'count': paginator})


def user_add(request):
    """
    新增用户
    :param request:
    :return:
    """
    return render(request, 'pages/org/user/user-add.html')


def user_edit(request, u_edit):
    """
    用户信息修改
    :param request:
    :return:
    """
    if request.method == 'GET':
        user_one = UserRole.objects.get(user_id=u_edit)  # 获取
        role = Role.objects.all()
        user = User.objects.get(user_id=u_edit)
        return render(request, 'pages/org/user/user-edit.html', {'user_one': user_one, 'role': role, 'user': user})
    else:
        user_logname = request.POST.get('user_logname')  # 获取登录账号
        user_password = request.POST.get('user_password')  # 获取登录密码
        user_realname = request.POST.get('user_realname')  # 获取用户名称
        user_Idcard = request.POST.get('user_Idcard')  # 获取用户身份证
        user_sex = request.POST.get('user_sex')  # 获取用户性别
        user_addres = request.POST.get('user_addres')  # 获取用户地址
        user_email = request.POST.get('user_email')  # 获取用户email
        user_phone = request.POST.get('user_phone')  # 获取用户手机号
        status = request.POST.get('status')  # 获取用户权限
        role_name = request.POST.get('role_name')  # 获取用户担任角色
        # user_one = UserRole.objects.get(user_id=u_edit)  # 获取
        user = User.objects.get(user_id=u_edit)
        user.user_logname = user_logname
        user.user_password = user_password
        user.user_realname = user_realname
        user.user_Idcard = user_Idcard
        user.user_sex = user_sex
        user.user_addres = user_addres
        user.user_email = user_email
        user.user_phone = user_phone
        user.status = status
        print(user_logname, user_password, user_realname, user_Idcard, user_sex, user_addres, user_email, user_phone,
              status, role_name)
        # user.save()
        # return render(request, 'pages/org/user/user-edit.html')
        return redirect('/org/user_edit/' + str(u_edit))


def user_delete(request, u_delete):
    """
    删除用户
    :param request:
    :return:
    """
    UserRole.objects.filter(user_id=u_delete).delete()  # 删除 选中用户
    return redirect('/org/org_user_index/')


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
