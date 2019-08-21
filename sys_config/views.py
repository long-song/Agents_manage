from django.shortcuts import render,redirect,reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from .models import *

# Create your views here.
def finType_add(request):
    '''
    访问财务类型添加
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'pages/sys_config/finaceType/finType-add.html')
    else:
        finacetype=request.POST.get('finacetype')
        state=request.POST.get('state')
        # print('finacetype=',finacetype,'state=',state)
        fintype=FinaceTb.objects.create(finacetype=finacetype,state=state,isdelete=0)
        fintype.save()
        return redirect(reverse('finType_list'))

def finType_edit(request):
    '''
    访问财务类型编辑
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        fintype=FinaceTb.objects.get(id=id)
        return render(request,'pages/sys_config/finaceType/finType-edit.html',{'fintype':fintype})
    else:
        id=request.POST.get('id')
        finacetype=request.POST.get('finacetype')
        state=request.POST.get('state')
        fintype=FinaceTb.objects.get(id=id)
        # fintype=FinaceTb()
        fintype.finacetype=finacetype
        fintype.state=state
        fintype.save()
        return redirect(reverse('finType_list'))



def finType_info(request):
    '''
    访问财务类型信息
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        fintype=FinaceTb.objects.get(id=id)
        return render(request, 'pages/sys_config/finaceType/finType-info.html',{'fintype':fintype})
    else:
        id = request.POST.get('id')
        finacetype = request.POST.get('finacetype')
        state = request.POST.get('state')
        fintype = FinaceTb.objects.get(id=id)
        fintype.finacetype = finacetype
        fintype.state = state
        return redirect(reverse('finType_list'))

def finType_del(request):
    '''
    访问财务类型删除
    :param request:
    :return:
    '''
    if request.is_ajax():
        id = request.POST.get('id')
        fintype = FinaceTb.objects.get(id=id)
        fintype.delete()
        return JsonResponse({'del': '删除成功'})

def finType_list(request):
    '''
    访问财务类型
    :param request:
    :return:
    '''
    if request.method == 'GET':
        res = FinaceTb.objects.all()
        paginator = Paginator(res, 4)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('finTyep-list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/sys_config/finaceType/finType-list.html',
                      {'page': number, 'paginator': paginator})

    if request.is_ajax():
        id = request.POST.get('id')
        state = request.POST.get('state')
        state1 = 0
        if state == '启用':
            state1 = 1
        fintype = FinaceTb.objects.get(id=id)
        fintype.state = state1
        fintype.save()
        print('1')
        return JsonResponse({'state': '已%s' % state})



def sertype_add(request):
    '''
    服务类型添加
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'pages/sys_config/serviceType/serType-add.html')
    else:
        svctype=request.POST.get('svctype')
        money=request.POST.get('money')
        state=request.POST.get('state')
        # print('finacetype=',finacetype,'state=',state)
        sertype=ServinceTb.objects.create(svctype=svctype,money=money,state=state,caozuo=0)
        sertype.save()
        return redirect(reverse('sertype_list'))



def sertype_edit(request):
    '''
    服务类型编辑
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        sertype=ServinceTb.objects.get(id=id)
        return render(request,'pages/sys_config/serviceType/serType-edit.html',{'sertype':sertype})
    else:
        id=request.POST.get('id')
        svctype = request.POST.get('svctype')
        money = request.POST.get('money')
        state = request.POST.get('state')
        sertype=ServinceTb.objects.get(id=id)
        sertype.svctype=svctype
        sertype.money=money
        sertype.state=state
        sertype.save()
        return redirect(reverse('sertype_list'))



def sertype_info(request):
    '''
    服务类型详情
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        sertype=ServinceTb.objects.get(id=id)
        return render(request,'pages/sys_config/serviceType/serType-info.html',{'sertype':sertype})
    else:
        id=request.POST.get('id')
        svctype = request.POST.get('svctype')
        money = request.POST.get('money')
        state = request.POST.get('state')
        sertype=ServinceTb.objects.get(id=id)
        sertype.svctype=svctype
        sertype.money=money
        sertype.state=state
        return redirect(reverse('sertype_list'))



def sertype_list(request):
    '''
    服务类型管理
    :param request:
    :return:
    '''
    if request.method == 'GET':
        res = ServinceTb.objects.all()
        paginator = Paginator(res, 4)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('serType-list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/sys_config/serviceType/serType-list.html',
                      {'page': number, 'paginator': paginator})

    if request.is_ajax():
        id = request.POST.get('id')
        state = request.POST.get('state')
        state1 = 0
        if state == '启用':
            state1 = 1
        sertype = ServinceTb.objects.get(id=id)
        sertype.state = state1
        sertype.save()
        print('1')
        return JsonResponse({'state': '已%s' % state})



def service_year(request):
    '''
    服务年限
    :param request:
    :return:
    '''
    if request.method=='GET':
        service=SerYearTb.objects.get(id=1)
        return render(request,'pages/sys_config/serviceType/service-year.html',{'service':service})
    else:

        ser_name = request.POST.get('ser_name')
        ser_year = request.POST.get('ser_year')
        service=SerYearTb.objects.get(id=1)
        service.ser_name=ser_name
        service.ser_year=ser_year

        service.save()
        return redirect(reverse('service_year'))



def customerType_edit(request):
    '''
    客户类型编辑
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        customertype=CustomertypeTb.objects.get(id=id)
        return render(request, 'pages/sys_config/customerType/customerType-edit.html',{'customertype':customertype})
    else:
        id=request.POST.get('id')
        cstmtype=request.POST.get('cstmtype')
        state=request.POST.get('state')
        customertype=CustomertypeTb.objects.get(id=id)
        customertype.cstmtype=cstmtype
        customertype.state=state
        customertype.save()
        return redirect(reverse('customerType_list'))




def customerType_add(request):
    '''
    客户类型添加
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'pages/sys_config/customerType/customerType-add.html')
    else:
        cstmtype=request.POST.get('cstmtype')
        state=request.POST.get('state')
        customertype=CustomertypeTb.objects.create(cstmtype=cstmtype,state=state,isdelete=0)
        customertype.save()
        return redirect(reverse('customerType_list'))



def customerType_info(request):
    '''
    客户类型信息
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        customertype=CustomertypeTb.objects.get(id=id)
        return render(request, 'pages/sys_config/customerType/customerType-info.html',{'customertype':customertype})
    else:
        id=request.POST.get('id')
        cstmtype=request.POST.get('cstmtype')
        state=request.POST.get('state')
        customertype=CustomertypeTb.objects.get(id=id)
        customertype.cstmtype=cstmtype
        customertype.state=state
        return redirect(reverse('customerType_list'))




def customerType_del(request):
    """
    删除客户类型信息
    :param request:
    :return:
    """
    if request.is_ajax():
        id = request.POST.get('id')
        customertype = CustomertypeTb.objects.get(id=id)
        customertype.delete()
        return JsonResponse({'del': '删除成功'})


def customerType_list(request):
    '''
    客户类型管理
    :param request:
    :return:
    '''
    if request.method == 'GET':
        res = CustomertypeTb.objects.all()
        paginator = Paginator(res, 4)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('customerType-list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/sys_config/customerType/customerType-list.html',
                      {'page': number, 'paginator': paginator})

    if request.is_ajax():
        id = request.POST.get('id')
        state = request.POST.get('state')
        state1 = 0
        if state == '启用':
            state1 = 1
        customertype = CustomertypeTb.objects.get(id=id)
        customertype.state = state1
        customertype.save()
        print('1')
        return JsonResponse({'state': '已%s' % state})


def license_edit(request):
    '''
    证件类型编辑
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        license=LicenseTb.objects.get(id=id)
        return render(request, 'pages/sys_config/license/license-edit.html',{'license':license})
    else:
        id=request.POST.get('id')
        licstype=request.POST.get('licstype')
        state=request.POST.get('state')
        license=LicenseTb.objects.get(id=id)
        license.licstype=licstype
        license.state=state
        license.save()
        return redirect(reverse('license_list'))



def license_add(request):
    '''
    证件类型添加
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'pages/sys_config/license/license-add.html')
    else:
        licstype=request.POST.get('licstype')
        state=request.POST.get('state')
        license=LicenseTb.objects.create(licstype=licstype,state=state,isdelete=0)
        license.save()
        return redirect(reverse('license_list'))



def license_info(request):
    '''
    证件类型信息
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        license=LicenseTb.objects.get(id=id)
        return render(request, 'pages/sys_config/license/license-info.html',{'license':license})
    else:
        id=request.POST.get('id')
        licstype=request.POST.get('licstype')
        state=request.POST.get('state')
        license=LicenseTb.objects.get(id=id)
        license.licstype=licstype
        license.state=state
        return redirect(reverse('license_list'))


def license_del(request):
    """
    删除证件类型信息
    :param request:
    :return:
    """
    if request.is_ajax():
        id = request.POST.get('id')
        license = LicenseTb.objects.get(id=id)
        license.delete()
        return JsonResponse({'del': '删除成功'})

def license_list(request):
    '''
    证件类型管理
    :param request:
    :return:
    '''
    if request.method == 'GET':
        res = LicenseTb.objects.all()
        paginator = Paginator(res, 4)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('license-list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/sys_config/license/license-list.html',
                      {'page': number, 'paginator': paginator})

    if request.is_ajax():
        id = request.POST.get('id')
        state = request.POST.get('state')
        state1 = 0
        if state == '启用':
            state1 = 1
        license = LicenseTb.objects.get(id=id)
        license.state = state1
        license.save()
        print('1')
        return JsonResponse({'state': '已%s' % state})




def app_edit(request):
    '''
    访问
    :param request:
    :return:
    '''
    if request.method=='GET':
        app=AppTb.objects.get(id=1)
        return render(request, 'pages/sys_config/app/app-edit.html',{'app':app})
    else:
        aname = request.POST.get('aname')
        anumber = request.POST.get('anumber')
        app=AppTb.objects.get(id=1)
        app.aname=aname
        app.anumber=anumber

        app.save()
        return redirect(reverse('app_edit'))




def discount_add(request):
    '''
    优惠类型添加
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'pages/sys_config/discount/discount-add.html')
    else:
        dscttype=request.POST.get('dscttype')
        dsctyear=request.POST.get('dsctyear')
        realyear=request.POST.get('realyear')
        state=request.POST.get('state')
        discount=DiscountTb.objects.create(dscttype=dscttype,dsctyear=dsctyear,realyear=realyear,state=state,isdelete=0)
        discount.save()
        return redirect(reverse('discount_list'))



def discount_edit(request):
    '''
    优惠类型编辑
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        discount=DiscountTb.objects.get(id=id)
        return render(request, 'pages/sys_config/discount/discount-edit.html',{'discount':discount})
    else:
        id=request.POST.get('id')
        dscttype=request.POST.get('dscttype')
        dsctyear = request.POST.get('dsctyear')
        realyear = request.POST.get('realyear')
        state=request.POST.get('state')
        discount=DiscountTb.objects.get(id=id)
        discount.dscttype=dscttype
        discount.dsctyear=dsctyear
        discount.realyear=realyear
        discount.state=state
        discount.save()
        return redirect(reverse('discount_list'))



def discount_info(request):
    '''
    优惠类型信息
    :param request:
    :return:
    '''
    if request.method=='GET':
        id=request.GET.get('id')
        discount=DiscountTb.objects.get(id=id)
        return render(request, 'pages/sys_config/discount/discount-info.html',{'discount':discount})
    else:
        id=request.POST.get('id')
        dscttype=request.POST.get('dscttype')
        dsctyear = request.POST.get('dsctyear')
        realyear = request.POST.get('realyear')
        state=request.POST.get('state')
        discount=DiscountTb.objects.get(id=id)
        discount.dscttype=dscttype
        discount.dsctyear=dsctyear
        discount.realyear=realyear
        discount.state=state
        return redirect(reverse('discount_list'))


def discount_del(request):
    """
    删除优惠类型信息
    :param request:
    :return:
    """
    if request.is_ajax():
        id = request.POST.get('id')
        discount = DiscountTb.objects.get(id=id)
        discount.delete()
        return JsonResponse({'del': '删除成功'})

def discount_list(request):
    '''
    优惠类型管理
    :param request:
    :return:
    '''
    if request.method == 'GET':
        res = DiscountTb.objects.all()
        paginator = Paginator(res, 4)
        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取index的值，如果没有，则设置使用默认值1
            num = request.GET.get('discount-list', '1')
            # 获取第几页
            number = paginator.page(num)
            # print(number,type(number),num,type(num))
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

        # 将当前页页码，以及当前页数据传递到customer-list.html
        return render(request, 'pages/sys_config/discount/discount-list.html',
                      {'page': number, 'paginator': paginator})

    if request.is_ajax():
        id = request.POST.get('id')
        state = request.POST.get('state')
        state1 = 0
        if state == '启用':
            state1 = 1
        discount = DiscountTb.objects.get(id=id)
        discount.state = state1
        discount.save()
        print('1')
        return JsonResponse({'state': '已%s' % state})

