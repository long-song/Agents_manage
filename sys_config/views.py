from django.shortcuts import render


# Create your views here.
def finType_add(request):
    '''
    访问财务类型添加
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/finaceType/finType-add.html')


def finType_edit(request):
    '''
    访问财务类型编辑
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/finaceType/finType-edit.html')


def finType_info(request):
    '''
    访问财务类型信息
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/finaceType/finType-info.html')


def finType_list(request):
    '''
    访问财务类型
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/finaceType/finType-list.html')


def sertype_add(request):
    '''
    服务类型添加
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/serviceType/serType-add.html')


def sertype_edit(request):
    '''
    服务类型编辑
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/serviceType/sertype-edit.html')


def sertype_info(request):
    '''
    服务类型详情
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/serviceType/serType-info.html')


def sertype_list(request):
    '''
    服务类型管理
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/serviceType/serType-list.html')


def service_year(request):
    '''
    服务年限
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/serviceType/service-year.html')


def customerType_edit(request):
    '''
    客户类型编辑
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/customerType/customerType-edit.html')


def customerType_add(request):
    '''
    客户类型添加
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/customerType/customerType-add.html')


def customerType_info(request):
    '''
    客户类型信息
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/customerType/customerType-info.html')


def customerType_list(request):
    '''
    客户类型管理
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/customerType/customerType-list.html')


def license_edit(request):
    '''
    证件类型编辑
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/license/license-edit.html')


def license_add(request):
    '''
    证件类型添加
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/license/license-add.html')


def license_info(request):
    '''
    证件类型信息
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/license/license-info.html')


def license_list(request):
    '''
    证件类型管理
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/license/license-list.html')


def app_edit(request):
    '''
    访问
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/app/app-edit.html')


def discount_add(request):
    '''
    优惠类型添加
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/discount/discount-add.html')


def discount_edit(request):
    '''
    优惠类型编辑
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/discount/discount-edit.html')


def discount_info(request):
    '''
    优惠类型信息
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/discount/discount-info.html')


def discount_list(request):
    '''
    优惠类型管理
    :param request:
    :return:
    '''
    return render(request, 'pages/sys_config/discount/discount-list.html')
