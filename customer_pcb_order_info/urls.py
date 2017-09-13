from django.conf.urls import url

from . import views

urlpatterns = [
    # pcb订单 新增
    url(r'^add/$', views.add, name='add'),
    # ID 查询订单详情
    url(r'^get/(.+)/$', views.get, name='get'),
    # ID 查询订单 PCB 文件
    url(r'^pcb_down/(.+)/$', views.pcb_down, name='pcb_down'),
    # 客户 获取自己订单
    url(r'^list/by_customer/(\d+)/(\d+)/$', views.get_by_customer_id, name='get_by_customer_id'),
]
