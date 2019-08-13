from django.urls import path
from report import views

urlpatterns = [
    path('report_list/', views.report_list, name='report_list'),  # 访问报表管理路由
]
