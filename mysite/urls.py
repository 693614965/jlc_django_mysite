"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  url(r'^$', views.index, name='index'),  # 客户首页
                  url(r'^login/', views.login, name='login'),  # 客户登录页面
                  url(r'^client/', views.client, name='client'),  # 客户平台页面
                  url(r'^user/', include('user.urls')),  # 系统用户
                  url(r'^dict/', include('dict.urls')),  # 系统字典
                  url(r'^customer_info/', include('customer_info.urls')),  # 客户信息
                  url(r'^customer_pcb_data_info/', include('customer_pcb_data_info.urls')),  # 客户 PCB 资料信息
                  url(r'^customer_delivery_address_info/', include('customer_delivery_address_info.urls')),  # 客户收货地址信息
                  url(r'^customer_pcb_order_info/', include('customer_pcb_order_info.urls')),  # 客户PCB 订单信息
                  url(r'^steel_produce_info/', include('steel_produce_info.urls')),  # 钢网产品信息
                  url(r'^customer_steel_order_info/', include('customer_steel_order_info.urls')),  # 客户钢网订单信息
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
