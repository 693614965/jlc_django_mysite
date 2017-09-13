from django.db import models


class CustomerDeliveryAddress(models.Model):
    class Meta:
        db_table = 't_customer_delivery_address_info'
        verbose_name = '客户收货地址信息表'

    id = models.CharField(max_length=255, primary_key=True)
    link_man = models.CharField(max_length=255, verbose_name='联系人')
    link_man_mobile = models.CharField(max_length=255, verbose_name='联系人手机')
    province = models.CharField(max_length=255, verbose_name='省')
    city = models.CharField(max_length=255, verbose_name='市')
    area = models.CharField(max_length=255, verbose_name='街区')
    detail = models.CharField(max_length=255, verbose_name='地址详情')
    is_default = models.BooleanField(default=False, verbose_name='是否默认收货地址')
    customer_id = models.CharField(max_length=255, verbose_name='客户ID')
