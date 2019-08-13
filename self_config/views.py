from django.shortcuts import render


# Create your views here.
def login(request):
    '''
    访问登录页面
    :param request:
    :return:
    '''

    return render(request, 'login.html')


def main(request):
    '''
    访问主页
    :param request:
    :return:
    '''
    return render(request, 'main.html')

def password(request):
    '''
    访问当前登录用户修改密码
    :param request:
    :return:
    '''
    return render(request, 'pages/self_config/password.html')

def self_user_edit(request):
    '''
    访问当前登录用户个人资料修改
    :param request:
    :return:
    '''
    return render(request, 'pages/self_config/user-edit.html')

def self_user_info(request):
    '''
    访问当前登录用户个人信息
    :param request:
    :return:
    '''
    return render(request, 'pages/self_config/user-info.html')

def self_user_pic(request):
    '''
    访问当前登录用户头像
    :param request:
    :return:
    '''
    return render(request, 'pages/self_config/user-pic.html')

