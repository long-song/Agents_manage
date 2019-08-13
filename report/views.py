from django.shortcuts import render, HttpResponse


# Create your views here.
def report_list(request):
    """
    访问报表管理的列表功能
    :param request:
    :return:
    """

    return render(request, 'pages/report/report-list.html')
