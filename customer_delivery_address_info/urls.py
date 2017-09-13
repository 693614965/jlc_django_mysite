from django.conf.urls import url

from . import views

urlpatterns = [
    # 新增
    url(r'^add/$', views.add, name='add'),
    # 更新
    url(r'^update/$', views.update, name='update'),
    # 删除
    url(r'^delete/(.+)/$', views.delete, name='delete'),
    # ID 查询
    url(r'^get/(.+)/$', views.get_by_id, name='get_by_id'),
    # 客户 查询 自己收货地址
    url(r'^list/$', views.customer_list, name='customer_list'),
    # 设置 默认
    url(r'^set/default/(.+)/$', views.set_default, name='set_default'),

]
