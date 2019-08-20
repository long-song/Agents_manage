# 自定义过滤器
# 过滤器的本质其实就是python中的函数
from django.template import Library

# 创建一个library类的对象
register = Library()

# 自定义过滤器至少有一个参数，最多2个
@register.filter  # 将函数装饰成python中的过滤器进行使用
def mod(num):
    '''
    显示状态
    :param num:
    :return:
    '''
    if num == 0:
        return '禁用'
    else:
        return '启用'


@register.filter
def mod_val(num):
    '''判断num是否能被val整除'''
    if num == 0:
        return '启用'
    else:
        return '禁用'
