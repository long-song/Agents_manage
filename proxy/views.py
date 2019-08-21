from django.shortcuts import render, redirect, reverse, HttpResponse
from proxy.models import *
from django.http import JsonResponse
from sys_config.models import LicenseTb, CustomertypeTb, FinaceTb
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F, Q
import json


# Create your views here.
# 代理商客户管理列表
def customer_list(request):
    '''
    访问代理商客户管理列表
    :param request:
    :return:
    '''
    # 展示代理商客户信息及分页
    if request.method == 'GET':
        customer_list = Company.objects.all()
        paginator = Paginator(customer_list, 8)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('customer-list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/proxy/customer/customer-list.html',
                      {'page': number, 'paginator': paginator, 'method': 'GET'})
        # ajax请求修改状态功能
    if request.is_ajax():
        cid = request.POST.get('cid')
        state = request.POST.get('state')
        # print('cid',cid)
        # print('state',state)
        state1 = 0
        if state == '启用':
            state1 = 1
        customer = Company.objects.get(cid=cid)
        customer.state = state1
        customer.save()
        print('1')
        return JsonResponse({'state': '已%s' % state})


# 代理商客户查找
def customer_find(request):
    textfiled = request.GET.get('textfiled')
    print(textfiled)
    customer_list = Company.objects.filter(cname__contains=textfiled)
    if customer_list:
        paginator = Paginator(customer_list, 8)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('customer_find', '1')
            # 获取第几页
            number = paginator.page(num)
            request.session['textfiled'] = textfiled
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/proxy/customer/customer-list.html',
                      {'page': number, 'paginator': paginator, 'textfiled': textfiled})
    else:
        return render(request, 'pages/proxy/customer/customer-list.html', {'errmsg': '请填写正确的客户名称'})


# 代理商客户添加 / 联系人添加
def customer_add(request):
    '''
    访问代理商客户添加
    :param request:
    :return:
    '''
    if request.is_ajax():
        # 获取所有启用的企业类型 & 证件类型
        tids = CustomertypeTb.objects.filter(state=1)
        licsType = LicenseTb.objects.filter(state=1)
        tid_list = []
        lics_list = []
        for tid in tids:
            tid_list.append((tid.id, tid.cstmtype))
        for lics in licsType:
            lics_list.append((lics.id, lics.licstype))
        # print(tid_list)
        # print(lics_list)
        return JsonResponse({'tid': tid_list, 'lics': lics_list})
    if request.method == 'POST':
        cname = request.POST.get('cname')
        tid = request.POST.get('tid')
        state = request.POST.get('state')
        lowyer = request.POST.get('lowyer')
        licenseid = request.POST.get('licenseid')
        country = request.POST.get('country')
        fax = request.POST.get('fax')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        regtime = request.POST.get('regtime')
        licensecard = request.POST.get('licensecard')
        sheng = Province.objects.get(code_p=request.POST.get('sheng')).name
        shi = City.objects.get(code_c=request.POST.get('shi')).name
        qu = Area.objects.get(code_a=request.POST.get('qu')).name
        remark = request.POST.get('remark')
        print(locals())
        company = Company.objects.create()
        company.cname = cname
        company.tid = CustomertypeTb.objects.get(id=tid)
        company.state = state
        company.lowyer = lowyer
        company.licenseid = LicenseTb.objects.get(id=licenseid)
        company.fax = fax
        company.country = country
        company.phone = phone
        company.address = address
        company.regtime = regtime
        company.licensecard = licensecard
        company.sheng = sheng
        company.shi = shi
        company.qu = qu
        company.remark = remark
        company.save()
        lxname = request.POST.get('lxname')
        phone = request.POST.get('phone')
        fax = request.POST.get('fax')
        email = request.POST.get('email')
        department = request.POST.get('department')
        cid = Company.objects.get(cname=cname)
        lianxiren = Lianxiren.objects.create()
        lianxiren.lxname = lxname
        lianxiren.phone = phone
        lianxiren.fax = fax
        lianxiren.email = email
        lianxiren.department = department
        lianxiren.cid = cid
        lianxiren.save()
        return redirect(reverse('customer_list'))
    return render(request, 'pages/proxy/customer/customer-add.html')


# 省份管理器
def province(request):
    '''
    获取省联动信息
    :param request:
    :param p_id:
    :return:
    '''
    if request.is_ajax():
        infos_list = []
        infos = Province.objects.all()
        for info in infos:
            infos_list.append({'parentid': info.code_p, 'cityname': info.name})
        return JsonResponse({'infos': infos_list})


# 城市管理器
def city(request):
    '''
    获取市联动信息
    :param request:
    :param p_id:
    :return:
    '''
    if request.is_ajax():
        p_id = request.POST.get('p_id')
        print('p_id=' + p_id)
        sheng = Province.objects.get(code_p=p_id)
        print('sheng', sheng, type(sheng.name))
        infos_list = []
        infos = City.objects.filter(code_p=p_id)
        for info in infos:
            infos_list.append({'parentid': info.code_c, 'cityname': info.name})
        return JsonResponse({'infos': infos_list, 'address': sheng.name})


# 区县管理器
def area(request):
    '''
    获取区县联动信息
    :param request:
    :param p_id:
    :return:
    '''
    if request.is_ajax():
        p_id = request.POST.get('p_id')
        sheng = request.POST.get('sheng')
        # print('p_id=' + p_id)
        sheng = Province.objects.get(code_p=sheng)
        city = City.objects.get(code_c=p_id)
        infos_list = []
        infos = Area.objects.filter(code_c=p_id)
        for info in infos:
            infos_list.append({'parentid': info.code_a, 'cityname': info.name})
        return JsonResponse({'infos': infos_list, 'address': sheng.name + ' ' + city.name})


# 地址获取
def address(request):
    '''
    拼接地址
    :param request:
    :return:
    '''
    if request.is_ajax():
        province_id = request.POST.get('province_id')
        city_id = request.POST.get('city_id')
        area_id = request.POST.get('area_id')
        # print('p_id=' + p_id)
        sheng = Province.objects.get(code_p=province_id)
        city = City.objects.get(code_c=city_id)
        area = Area.objects.get(code_a=area_id)
        return JsonResponse({'address': sheng.name + ' ' + city.name + ' ' + area.name})


# 代理商充值
def customer_charge(request):
    '''
    访问代理商客户充值
    :param request:
    :return:
    '''
    if request.method == 'GET':
        cid = request.GET.get('id')
        charge = Company.objects.get(cid=cid)
        # print(charge,type(charge))
        return render(request, 'pages/proxy/customer/customer-charge.html', {'charge': charge})
    if request.is_ajax():
        cid = request.POST.get('cid')
        balance_add = int(request.POST.get('balance_add'))
        charge = Company.objects.get(cid=cid)
        print(type(balance_add))
        charge.balance += balance_add
        charge.save()
        return JsonResponse({'message': '充值成功', 'balance': charge.balance})


# 代理商客户信息编辑
def customer_edit(request):
    '''
    访问代理商客户编辑
    :param request:
    :return:
    '''
    if request.method == 'GET':
        cid = request.GET.get('id')
        company = Company.objects.get(cid=cid)
        return render(request, 'pages/proxy/customer/customer-edit.html', {'company': company})
    if request.method == 'POST':
        cid = request.POST.get('cid')
        cname = request.POST.get('cname')
        tid = request.POST.get('tid')
        state = request.POST.get('state')
        lowyer = request.POST.get('lowyer')
        fax = request.POST.get('fax')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        sheng = Province.objects.get(code_p=request.POST.get('sheng')).name
        shi = City.objects.get(code_c=request.POST.get('shi')).name
        qu = Area.objects.get(code_a=request.POST.get('qu')).name
        remark = request.POST.get('remark')
        print(locals())
        company = Company.objects.get(cid=cid)
        company.cname = cname
        company.tid = CustomertypeTb.objects.get(id=tid)
        company.state = state
        company.lowyer = lowyer
        company.fax = fax
        company.phone = phone
        company.address = address
        company.sheng = sheng
        company.shi = shi
        company.qu = qu
        company.remark = remark
        company.save()
        return redirect(reverse('customer_list'))


# 代理商客户信息
def customer_info(request):
    '''
    访问代理商客户信息
    :param request:
    :return:
    '''
    if request.method == 'GET':
        cid = request.GET.get('id')
        company = Company.objects.get(cid=cid)
        lianxiren = Lianxiren.objects.filter(cid=company)
        return render(request, 'pages/proxy/customer/customer-info.html', {'company': company, 'lianxiren': lianxiren})


# 代理商客户删除
def customer_del(request):
    '''
    访问代理商客户删除
    :param request:
    :return:
    '''
    if request.is_ajax():
        cid = request.POST.get('cid')
        company = Company.objects.get(cid=cid)
        company.delete()
        return JsonResponse({'del': '删除成功'})


# 代理商预付款管理
def customerPay_list(request):
    '''
    访问代理商预付款管理
    :param request:
    :return:
    '''
    if request.is_ajax():
        finacetype_list = []
        finacetype = FinaceTb.objects.filter(state=1)
        for info in finacetype:
            finacetype_list.append({'id': info.id, 'finacetype': info.finacetype})
        return JsonResponse({'finacetypes': finacetype_list})
    if request.method == 'GET':
        customerPay = Prepayment.objects.all()
        paginator = Paginator(customerPay, 8)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('customer-Pay', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/proxy/customerPay/proxy-list.html',
                      {'page': number, 'paginator': paginator, 'method': 'get'})


# 代理商预付款信息查找
def customerPay_find(request):
    '''
    访问代理商预付款管理
    :param request:
    :return:
    '''
    finacetype = request.GET.get('finacetype')
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    print(locals())
    customerPay = Prepayment.objects.filter(finaceid=finacetype, datetime__range=(startDate, endDate))
    if customerPay:
        paginator = Paginator(customerPay, 8)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('customer-Pay', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/proxy/customerPay/proxy-list.html',
                      {'page': number, 'paginator': paginator, 'finacetype': finacetype, 'startDate': startDate,
                       'endDate': endDate})
    else:
        return render(request, 'pages/proxy/customerPay/proxy-list.html', {'errmsg': '请填写正确的客户名称'})


# 操作日志管理
def log_list(request):
    '''
    访问操作日志
    :param request:
    :return:
    '''
    if request.method == 'GET':
        log_list = Rizhi.objects.all()
        paginator = Paginator(log_list, 10)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('log_list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/proxy/log/log-list.html',
                      {'page': number, 'paginator': paginator, 'method': 'get'})


# 操作日志查找
def log_list_find(request):
    '''
    访问操作日志
    :param request:
    :return:
    '''
    rzname = request.GET.get('rzname')
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    print(locals())
    log_list = Rizhi.objects.filter(rzname=rzname,rztime__range=(startDate, endDate))
    paginator = Paginator(log_list, 10)
    if log_list:
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('log_list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/proxy/log/log-list.html',
                      {'page': number, 'paginator': paginator,'rzname':rzname, 'startDate': startDate,
                       'endDate': endDate})
    else:
        return render(request, 'pages/proxy/log/log-list.html', {'errmsg': '请填写正确的客户名称'})