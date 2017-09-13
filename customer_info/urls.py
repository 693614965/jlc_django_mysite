from django.conf.urls import url

from . import views

urlpatterns = [
    # 客户信息 新增
    url(r'^add/$', views.add, name='add'),
    # 客户信息 更新
    url(r'^update/$', views.update, name='update'),
    # 客户查询个人信息
    url(r'^get/personnel/$', views.get_personnel_info, name='get_personnel_info'),
    # 客户信息 ID 查询
    url(r'^get/(.+)/$', views.get_by_id, name='get_by_id'),
    # 客户信息 删除
    url(r'^delete/(.+)/$', views.delete, name='delete'),
    # 客户信息 分页查询
    url(r'^list/(\d+)/(\d+)/$', views.list, name='list'),

]
