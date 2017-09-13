from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^update/$', views.update, name='update'),
    url(r'^get/(.+)/$', views.get_by_id, name='get_by_id'),
    url(r'^list/$', views.list, name='list'),
]
