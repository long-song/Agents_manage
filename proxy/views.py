from django.shortcuts import render


# Create your views here.
def customer_list(request):
    '''
    访问代理商客户管理列表
    :param request:
    :return:
    '''
    return render(request, 'pages/proxy/customer/customer-list.html')


def customer_add(request):
    '''
    访问代理商客户添加
    :param request:
    :return:
    '''
    return render(request, 'pages/proxy/customer/customer-add.html')


def customer_charge(request):
    '''
    访问代理商客户充值
    :param request:
    :return:
    '''
    return render(request, 'pages/proxy/customer/customer-charge.html')


def customer_edit(request):
    '''
    访问代理商客户编辑
    :param request:
    :return:
    '''
    return render(request, 'pages/proxy/customer/customer-edit.html')


def customer_info(request):
    '''
    访问代理商客户信息
    :param request:
    :return:
    '''
    return render(request, 'pages/proxy/customer/customer-info.html')

def customerPay_list(request):
    '''
    访问代理商预付款管理
    :param request:
    :return:
    '''
    return render(request, 'pages/proxy/customerPay/proxy-list.html')

def log_list(request):
    '''
    访问操作日志
    :param request:
    :return:
    '''
    return render(request, 'pages/proxy/log/log-list.html')