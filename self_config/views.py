from django.shortcuts import render, redirect, HttpResponse, reverse
from org.models import User,UserRole
from org.models import Pic
from django import views
from django.db.models import F, Q
import os
import re
from .models import *
from django.conf import settings


# Create your views here.


# 登录验证函数
def login_required(view_func):
    """
    登录装饰器函数
    :return:
    """
    def wrapper(request, *args, **kwargs):
        if not request.session.has_key('is_login'):
            return redirect('login')

        return view_func(request, *args, **kwargs)

    return wrapper

def login(request):
    '''
    访问登录页面
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 接收客户端发送来的数据
        query_dict = request.POST
        logname = query_dict.get('user_logname')
        password = query_dict.get('user_password')
        print('user_logname=', logname, 'user_password=', password)
        # 2.校验数据的准确性
        # A: 校验数据是否输入内容:all([]):如果列表中所有的内容都不为空则返回True,否则返回False
        if not all([logname, password]):
            return render(request, 'login.html', {'errmsg': '请输入用户密码进行登陆！'})

        try:
            user = User.objects.get(user_logname=logname, user_password=password)  # 获取数据库用户密码
            password = user.user_password  # 密文
        except:
            return render(request, 'login.html', {'errmsg': '账号或密码错误'})
        # print('1')
        request.session["is_login"] = True  # 记录用户登陆
        request.session["user_logname"] = user.user_logname  # 记录用户登陆名

        return render(request, 'main.html')


@login_required
def logout(request):
    '''
    注销函数
    :param request:
    :return:
    '''
    request.session.flush()
    return redirect(reverse('login'))

def main(request):
    '''
    访问主页
    :param request:
    :return:
    '''
    path = os.path.join(settings.BASE_DIR, 'agents_manage')
    print('path=' + path)
    return render(request, 'main.html')


def password(request):
    '''
    访问当前登录用户修改密码
    :param request:
    :return:
    '''
    a = request.session['user_logname']
    user = User.objects.get(user_logname=a)
    if request.method == "GET":
        return render(request, 'pages/self_config/password.html', {'user': user})
    if request.method == "POST":
        old_pwd = request.POST.get('old_pwd')
        new_pwd = request.POST.get('new_pwd')
        new_pwd1 = request.POST.get('new_pwd1')
        if old_pwd == user.user_password:
            if new_pwd != old_pwd:
                if new_pwd == new_pwd1:
                    user.user_password = new_pwd
                    user.save()
                    # print('12')
                    request.session.flush()
                    message = '您的密码已修改成功！'
                    return render(request, 'login.html', {'meaasge': message})
                else:
                    message = '新密码输入不一致！'
            else:
                message = '新密码与原密码相同'
        else:
            message = '原密码输入错误！'
        return render(request, 'pages/self_config/password.html',{'message':message})


def self_user_edit(request):
    '''
    访问当前登录用户个人资料修改
    :param request:
    :return:
    '''

    if request.method == "GET":
        a = request.session['user_logname']
        user = User.objects.get(user_logname=a)
        a = user.user_id
        pic = Pic.objects.get(user_id=a)
        return render(request, 'pages/self_config/user-edit.html', {'user': user, 'pic':pic})
    if request.method == "POST":
        new_user_logname = request.POST.get('new_user_logname')
        new_user_realname = request.POST.get('new_user_realname')
        new_user_idcard = request.POST.get('new_user_idcard')
        new_user_sex = request.POST.get('new_user_sex')
        new_user_address = request.POST.get('new_user_address')
        new_user_email = request.POST.get('new_user_email')
        new_user_phone = request.POST.get('new_user_phone')
        print(new_user_logname, new_user_realname, new_user_idcard, new_user_sex, new_user_address, new_user_email, new_user_phone)
        a = request.session['user_logname']
        user = User.objects.get(user_logname=a)
        user.user_logname = new_user_logname
        user.user_realname = new_user_realname
        user.user_idcard = new_user_idcard
        user.user_sex = new_user_sex
        user.user_address = new_user_address
        user.user_email = new_user_email
        user.user_phone = new_user_phone
        user.save()
        return redirect('self_user_info')
    return render(request, 'pages/self_config/user-edit.html')



def self_user_info(request):
    """
    展示个人信息页面
    :param request:
    :return:
    """

    a = request.session['user_logname']
    print('a', a)
    user0 = User.objects.get(user_logname=a)

    print('user0', user0.user_id)
    a = user0.user_id
    pic = Pic.objects.get(user_id=a)
    # print(type(a))
    user = UserRole.objects.get(user_id=a)
    # print(user)
    # print('user', user)
    return render(request, 'pages/self_config/user-info.html', {'user': user, 'pic': pic})


def self_user_pic(request):
    '''
    访问当前登录用户头像
    :param request:
    :return:
    '''
    if request.method == "GET":
        a = request.session['user_logname']
        user = User.objects.get(user_logname=a)
        return render(request, 'pages/self_config/user-pic.html', {'user': user})
    if request.method == "POST":
        my_header = request.FILES.get('my_header')
        a = request.session['user_logname']
        user = User.objects.get(user_logname=a)
        print(my_header, user)
        # user.head_img = my_header
        # pic = Pic.objects.create(user_id=user.user_id,my_header=my_header)
        try:
            pic = Pic.objects.get(user_id=user.user_id)
        except:
            pic = Pic.objects.create(my_header=my_header,user_id=user.user_id)
        if my_header == None:
          return render(request, 'pages/self_config/user-pic.html', {'user': user})
        # pic = Pic.objects.get(user_id=user.user_id)
        # pic.id = user.user_id
        pic.my_header = my_header
        pic.user_id = user.user_id
        pic.save()
        return redirect('self_user_info')
    return render(request, 'pages/self_config/user-pic.html')
