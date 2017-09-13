from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^get/(.+)/$', views.get_by_id, name='get_by_id'),
    url(r'^list/(\d+)/(\d+)/$', views.list, name='list'),
    url(r'^update/(.+)/$', views.update, name='update'),
    url(r'^delete/(.+)/$', views.delete, name='delete'),
    url(r'^detail/add/$', views.detail_add, name='detail_add'),
    url(r'^detail/get/(.+)/$', views.detail_get_by_id, name='detail_get_by_id'),
    url(r'^detail/list/(\d+)/(\d+)/$', views.detail_list, name='detail_list'),
    url(r'^detail/update/(.+)/$', views.detail_update, name='detail_update'),
    url(r'^detail/delete/(.+)/$', views.detail_delete, name='detail_delete'),
]
