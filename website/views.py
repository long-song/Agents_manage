from django.shortcuts import render


# Create your views here.
def website_add(request):
    """
    访问门户的添加功能
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'pages/website/website-add.html')


def website_edit(request):
    """
    访问门户的编辑功能
    :param request:
    :return:
    """

    return render(request, 'pages/website/website-edit.html')


def website_info(request):
    """
    访问门户的信息功能
    :param request:
    :return:
    """

    return render(request, 'pages/website/website-info.html')


def website_list(request):
    """
    访问门户的列表功能
    :param request:
    :return:
    """

    return render(request, 'pages/website/website-list.html')
