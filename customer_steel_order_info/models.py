from django.db import models
from django.utils import timezone


class CustomerSteelOrderInfo(models.Model):
    class Meta:
        db_table = 't_customer_steel_order_info'
        verbose_name = '客户钢网订单信息'

    id = models.CharField(max_length=255, primary_key=True)
    # 客户下单 时 选择的PCB 订单ID
    customer_pcb_order_id = models.CharField(max_length=255, verbose_name='客户选择的PCB订单 ID')

    # 客户下单时选择的钢网信息
    spec = models.CharField(max_length=255, verbose_name='钢网规格')
    area = models.CharField(max_length=255, verbose_name='钢网有效面积')
    net_pay_price = models.CharField(max_length=255, verbose_name='网络支付价')
    express_coll_price = models.CharField(max_length=255, verbose_name='快递代收价')
    gross_weight = models.CharField(max_length=255, verbose_name='毛重')

    # 客户钢网订单 属性
    steel_number = models.IntegerField(verbose_name='下单钢网数目')
    required_pack = models.CharField(max_length=255, verbose_name='包装要求')
    required_receipt_and_delivery_note = models.CharField(max_length=255, verbose_name='是否需要收据和送货单')
    steel_use = models.CharField(max_length=255, verbose_name='用途')
    required_mark = models.CharField(max_length=255, verbose_name='MARK要求')
    polishing_process = models.CharField(max_length=255, verbose_name='抛光工艺')
    required_engineering_process = models.CharField(max_length=255, verbose_name='工程处理要求')
    remark = models.CharField(max_length=255, verbose_name='备注')
    date_order = models.DateTimeField(default=timezone.now, verbose_name='下单时间')
