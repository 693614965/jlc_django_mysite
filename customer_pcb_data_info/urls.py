from django.conf.urls import url

from . import views

urlpatterns = [
    # 客户资料新增
    url(r'^add/$', views.add, name='add'),
    # 客户资料更新
    url(r'^update/$', views.update, name='update'),
    # 客户资料 ID 查询
    url(r'^get/(.+)/$', views.get_by_id, name='get_by_id'),
    # 客户资料 删除
    url(r'^delete/(.+)/$', views.delete, name='delete'),
    # 提交pcb 资料 审核
    url(r'^check/(.+)/$', views.check, name='check'),
    # 客户上传PCB文件
    url(r'^pcb_upload/$', views.pcb_upload, name='pcb_upload'),
    # 客户下载PCB文件
    url(r'^pcb_down/(.+)/$', views.pcb_down, name='pcb_down'),
    # 客户资料 customer_id 查询 （查询客户自己的资料信息）
    url(r'^list/$', views.list_by_customer_id, name='list_by_customer_id'),
    # 分页查询客户资料
    url(r'^list/(\d+)/(\d+)/$', views.list, name='list'),
    # 查询 PCB 资料 下单 信息
    url(r'^get_order_info/(.+)/$', views.get__order_info, name='get__order_info'),
]
