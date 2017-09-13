from django.db import models


class SteelProduceInfo(models.Model):
    class Meta:
        db_table = 't_steel_produce_info'
        verbose_name = '钢网产品信息'

    id = models.CharField(max_length=255, primary_key=True)
    spec = models.CharField(max_length=255, verbose_name='钢网规格')
    area = models.CharField(max_length=255, verbose_name='钢网有效面积')
    net_pay_price = models.CharField(max_length=255, verbose_name='网络支付价')
    express_coll_price = models.CharField(max_length=255, verbose_name='快递代收价')
    gross_weight = models.CharField(max_length=255, verbose_name='毛重')
