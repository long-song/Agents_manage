from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View

from .models import *
from proxy.models import User
from django.core.paginator import Paginator
from sys_config.models import *
from report.models import *
from website.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re


# Create your views here.


def org_role_index(request, o_role=1, textfield23=1):
    """
    角色首页
    :param request:
    :return:
    """
    role_all = Role.objects.all()
    # role_all = RoleMenu.objects.all()
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
        print(role_name)
        try:
            Role.objects.get(role_name=role_name)
        except:
            status = request.POST.get('status')  # 获取角色状态
            role_remark = request.POST.get('role_remark')  # 获取角色备注
            if status == '1':
                role_isdel = '0'
            else:
                role_isdel = '1'
            Role.objects.create(role_name=role_name, role_state=status, role_remark=role_remark,
                                role_isdel=role_isdel)  # 添加
            print(role_name, status, role_remark)
            return redirect('/org/role_index/')
        else:
            return render(request, 'pages/org/role/role-add.html', {'name': '已存在'})


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
        state = StateTb.objects.all  # 权限
        return render(request, 'pages/org/role/role-edit.html', {'role_edit': role_edit, 'state': state})

    else:
        role_edit = Role.objects.get(role_id=edit)  # 获取单角色信息
        text = request.POST.get('text')  # 获取角色名称
        try:
            Role.objects.get(role_name=text)
        except:
            status = request.POST.get('status')
            remark = request.POST.get('remark')
            role_edit.role_name = text
            role_edit.role_state = status
            role_edit.role_remark = remark
            role_edit.save()
            print(edit, text, status, remark)
            # Role.objects.create(role_id=edit, role_name=text, role_state=status, role_remark=remark, role_isdel=1)
            return render(request, 'pages/org/role/role-edit.html', {'role_edit': role_edit})

        else:
            return render(request, 'pages/org/role/role-edit.html', {'role_edit': role_edit, 'name': '已存在'})


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


# @csrf_exempt
def menu_add(request):
    """
    新增菜单信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'pages/org/menu/menu-add.html')
    else:
        querydict = request.POST
        menu_name = querydict.get('menu_name')  # 菜单名称
        print(menu_name)
        # if menu_name == '系统管理':
        #     return JsonResponse({"status": 1})
        # else:
        #     return JsonResponse({'status': 0})
        try:
            menu_name = Menu.objects.get(menu_name=menu_name)
        except:
            select_menu = querydict.get('select_menu')  # 上级菜单
            status = querydict.get('status')  # 菜单权限
            menu_url = querydict.get('menu_url')  # 菜单路径
            try:
                menu_url = Menu.objects.get(menu_url=menu_url)
            except:

                menu_intro = querydict.get('menu_intro')  # 菜单简介
                if status == '1':
                    menu_isdel = '0'
                else:
                    menu_isdel = '1'
                print(menu_name, select_menu, status, menu_url, menu_intro, menu_isdel)

                Menu.objects.create(menu_name=menu_name, menu_firstmenu=select_menu, menu_state=status,
                                    menu_url=menu_url,
                                    menu_intro=menu_intro, menu_isdel=menu_isdel)
                #     return HttpResponse(menu_name, select_menu, status, menu_url, menu_intro, menu_isdel)
                return redirect('/org/org_menu_index/')
                # return JsonResponse({'state':0})

        return render(request, 'pages/org/menu/menu-add.html', {'menu_name': '已存在', 'menu_url': '不能重复'})
        # return JsonResponse({'state':1})


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
        state = StateTb.objects.all()
        return render(request, 'pages/org/menu/menu-edit.html', {'menu_one': menu_one, 'state': state})
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


# @csrf_exempt
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


class User_Add(View):
    """新增用户"""

    def get(self, request):
        """
        get请求
        :param request:
        :return:
        """
        role = Role.objects.all()  # 角色
        return render(request, 'pages/org/user/user-add.html', {'role': role})

    def post(self, request):
        """
        POST请求
        :param request:
        :return:
        """
        user_logname = request.POST.get('user_logname')  # 获取到用户的登录账号

        try:
            User.objects.get(user_logname=user_logname)
        except:
            user_password = request.POST.get('user_password')  # 获取到用户的登录密码
            password_re = re.search('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@!.%*#?&])[A-Za-z\d$@.!%*#?&]{8,}$', user_password)
            if password_re:
                user_realname = request.POST.get('user_realname')  # 获取到用户的名字
                realname_re = re.search('^[\u4E00-\u9FA5A-Za-z]+$', user_realname)
                if realname_re:
                    user_idcard = request.POST.get('user_Idcard')  # 获取到用户的身份
                    try:
                        User.objects.get(user_idcard=user_idcard)
                    except:
                        idacard_re = re.search(
                            '^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^'
                            '[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$',
                            user_idcard)
                        if idacard_re:
                            user_sex = request.POST.get('user_sex')  # 获取到用户的性别
                            user_address = request.POST.get('user_address')  # 获取到用户的地址
                            try:
                                User.objects.get(user_address=user_address)
                            except:
                                user_email = request.POST.get('user_email')  # 获取到用户的emial
                                try:
                                    User.objects.get(user_email=user_email)
                                except:
                                    email_re = re.search(
                                        '^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',
                                        user_email)
                                    if email_re:
                                        user_phone = request.POST.get('user_phone')  # 获取到用户的联系电话
                                        try:
                                            User.objects.get(user_phone=user_phone)
                                        except:
                                            phone_re = re.search(
                                                '^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$',
                                                user_phone)
                                            if phone_re:
                                                user_sate = request.POST.get('user_sate')  # 启用状态
                                                # UserRole.objects.create()  # 关联表
                                                User.objects.create(user_logname=user_logname,
                                                                    user_password=user_password,
                                                                    user_realname=user_realname,
                                                                    user_idcard=user_idcard, user_sex=user_sex,
                                                                    user_address=user_address, user_email=user_email,
                                                                    user_phone=user_phone, user_state=user_sate)
                                                print(user_logname, user_password, user_realname, user_idcard,
                                                      user_sex, user_address, user_email, user_phone,
                                                      user_sate)

                                                return redirect('/org/org_user_index/')
                                            else:
                                                return render(request, 'pages/org/user/user-add.html',
                                                              {"user_phone": '联系电话错误'})
                                        else:
                                            return render(request, 'pages/org/user/user-add.html',
                                                          {"user_phon": '联系电话不能重复'})

                                    else:
                                        return render(request, 'pages/org/user/user-add.html', {"user_email": '邮箱错误'})
                                else:
                                    return render(request, 'pages/org/user/user-add.html', {"user_emai": '邮箱不能重复'})
                            else:
                                return render(request, 'pages/org/user/user-add.html', {"user_address": '地址不存在'})

                        else:
                            return render(request, 'pages/org/user/user-add.html', {"user_idcard": '证件号错误'})
                    else:
                        return render(request, 'pages/org/user/user-add.html', {"user_idcar": '证件号不能重复'})
                else:
                    return render(request, 'pages/org/user/user-add.html', {"user_realname": '名称错误'})
            else:
                return render(request, 'pages/org/user/user-add.html', {"user_password": '密码格式错误'})

        else:
            return render(request, 'pages/org/user/user-add.html', {"user_logname": '已存在'})


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
        user_one = UserRole.objects.get(user_id=u_edit)  # 获取
        role = Role.objects.all()
        user = User.objects.get(user_id=u_edit)
        user_logname = request.POST.get('user_logname')  # 获取登录账号
        try:
            UserRole.objects.get(user__user_logname=user_logname)
        except:
            user_password = request.POST.get('user_password')  # 获取登录密码
            user_password_re = re.search("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@!.%*#?&])[A-Za-z\d$@.!%*#?&]{8,}$",
                                         user_password)
            if user_password_re == None:
                return render(request, 'pages/org/user/user-edit.html',
                              {'user_one': user_one, 'role': role, 'user': user,
                               'user_password': '至少8个字符，至少1个字母，1个数字和1个特殊字符'})
            else:
                user_realname = request.POST.get('user_realname')  # 获取用户名称
                user_realname_re = re.search("^[\u4E00-\u9FA5A-Za-z]+$", user_realname)
                if user_realname_re == None:
                    return render(request, 'pages/org/user/user-edit.html',
                                  {'user_one': user_one, 'role': role, 'user': user,
                                   'user_realname': '只能输入中文和英文'})
                user_Idcard = request.POST.get('user_Idcard')  # 获取用户身份证
                user_Idcard_re = re.search(
                    "^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$",
                    user_Idcard)
                if user_Idcard_re == None:
                    return render(request, 'pages/org/user/user-edit.html',
                                  {'user_one': user_one, 'role': role, 'user': user,
                                   'user_Idcard': '支持 15 位和 18 位身份证号'})
                user_sex = request.POST.get('user_sex')  # 获取用户性别
                if re.search('\d{2}', user_sex) == None:
                    return render(request, 'pages/org/user/user-edit.html',
                                  {'user_one': user_one, 'role': role, 'user': user,
                                   'user_sex': '必须为数字'})
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
                print(user_logname, user_password, user_realname, user_Idcard, user_sex, user_addres, user_email,
                      user_phone,
                      status, role_name)
                # user.save()
                # return render(request, 'pages/org/user/user-edit.html')
                return redirect('/org/user_edit/' + str(u_edit))
    return render(request, 'pages/org/user/user-edit.html',
                  {'user_one': user_one, 'role': role, 'user': user, 'user_logname': '已存在'})

    # return redirect('/org/user_edit/' + str(u_edit),{'user_logname':'已存在'})


def user_delete(request, u_delete):
    """
    删除用户
    :param request:
    :return:
    """
    UserRole.objects.filter(user_id=u_delete).delete()  # 删除 选中用户
    return redirect('/org/org_user_index/')


def user_off(request, u_off):
    """
    禁用用户
    :param request:
    :return:
    """
    user_state = User.objects.get(user_id=u_off)
    if user_state.user_state == 1:
        user_state.user_state = 0
        user_state.save()
        return redirect('/org/org_user_index/')
    else:
        return redirect('/org/org_user_index/')


def user_pay(request, u_pay):
    """
    用户预付款
    :param request:
    :return:
    """
    reportlist = ReportList.objects.all()  # 用户预付款信息
    finace = FinaceTb.objects.all()
    user_role = UserRole.objects.get(user__user_id=u_pay)  # 获取该用户名
    print(user_role.user.user_realname)
    paginator = Paginator(reportlist, 5)  # 分页  5条信息
    for rep in reportlist:
        re = rep
    return render(request, 'pages/org/user/user-pay.html',
                  {'reportlist': reportlist, 'user_role': user_role, 'finace': finace, 'count': paginator, 're': rep})


def user_pay_find(request, u_pay_find):
    """
    预付款查找
    :param request:
    :return:
    """
    if request.method == 'GET':
        return redirect('/org/user_pay/' + str(u_pay_find))
        # pass
    else:
        finace = FinaceTb.objects.all()  # 财务类型
        user_role = UserRole.objects.get(user__user_id=u_pay_find)  # 获取该用户名

        requery_set = request.POST
        finacetype = requery_set.get('finacetype')  # 获取财务类型
        rep_start_nowdate = requery_set.get('rep_nowdate')  # 获取起时间
        rep_stop_nowdate1 = requery_set.get('rep_nowdate1')  # 获取终时间

        print("起时间：", rep_start_nowdate)
        if rep_start_nowdate:
            # 如果有起时间 查找大于等于 起时间的
            reportlist = ReportList.objects.filter(rep_finatype__exact=finacetype,
                                                   rep_nowdate__gte=rep_start_nowdate)  # 用户预付款信息
        else:
            # 小于终时间的
            if rep_stop_nowdate1:
                reportlist = ReportList.objects.filter(rep_finatype__exact=finacetype,
                                                       rep_nowdate__lte=rep_stop_nowdate1)  # 用户预付款信息
            else:
                reportlist = ReportList.objects.all()  # 用户预付款信息
                return render(request, 'pages/org/user/user-pay.html',
                              {'reportlist': reportlist, 'user_role': user_role, 'finace': finace})
        print(finacetype)
        return render(request, 'pages/org/user/user-pay.html',
                      {'reportlist': reportlist, 'user_role': user_role, 'finace': finace})


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
