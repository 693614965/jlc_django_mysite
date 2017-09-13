from django.db import models
from django.utils import timezone


class CustomerPcbOrderInfo(models.Model):
    class Meta:
        db_table = 't_customer_pcb_order_info'
        verbose_name = '客户PCB订单信息表'

    id = models.CharField(max_length=255, primary_key=True)
    # 下单 提交 的 PCB 资料信息
    layer = models.IntegerField(verbose_name='层数')
    width = models.IntegerField(verbose_name='宽度')
    length = models.IntegerField(verbose_name='长度')
    board_area = models.IntegerField(verbose_name='板子面积')
    pcb_num = models.IntegerField(verbose_name='板子数量')
    thickness = models.FloatField(verbose_name='厚度')
    solder_color = models.CharField(max_length=255, verbose_name='阻焊颜色')
    char_color = models.CharField(max_length=255, verbose_name='字符颜色')
    pad_cover = models.CharField(max_length=255, verbose_name='焊盘覆盖')
    pad_spraying = models.CharField(max_length=255, verbose_name='喷镀')
    minute_test = models.CharField(max_length=255, verbose_name='飞针测试')
    delivery_time = models.CharField(max_length=255, verbose_name='发货时间')
    required_invoice = models.CharField(max_length=255, verbose_name='是否需要发票')
    required_add_customer_num = models.CharField(max_length=255, verbose_name='是否加客编')
    required_book = models.CharField(max_length=255, verbose_name='是否需要教材')
    required_add_date_in_pcs = models.CharField(max_length=255, verbose_name='是否在每个单片(PCS)内增加生产日期')
    required_wait_delivery_together = models.CharField(max_length=255, verbose_name='是否等待一起发货')
    required_pack = models.CharField(max_length=255, verbose_name='包装要求')
    required_receipt_and_delivery_note = models.CharField(max_length=255, verbose_name='是否需要收据和送货单')
    outside_barcode = models.CharField(max_length=255, verbose_name='生产条码是否放在外面')
    required_smt = models.CharField(max_length=255, verbose_name='是否需要SMT')
    required_steel = models.CharField(max_length=255, verbose_name='是否需要钢网')
    remarks = models.CharField(max_length=255, verbose_name='备注')
    pcb_file_name = models.CharField(max_length=255, verbose_name='pcb文件名称')
    pcb_file_url = models.CharField(max_length=255, verbose_name='pcb文件保存磁盘地址')
    customer_id = models.CharField(max_length=255, verbose_name='客户ID')

    # 收货地址信息
    link_man = models.CharField(max_length=255, verbose_name='联系人')
    link_man_mobile = models.CharField(max_length=255, verbose_name='联系人手机')
    province = models.CharField(max_length=255, verbose_name='省')
    city = models.CharField(max_length=255, verbose_name='市')
    area = models.CharField(max_length=255, verbose_name='街区')
    detail = models.CharField(max_length=255, verbose_name='地址详情')

    # 订单额外 属性
    number_order = models.CharField(max_length=255, verbose_name='订单编号')
    total_amount = models.FloatField(verbose_name='订单总金额')
    order_status = models.IntegerField(verbose_name='订单状态', default=0)
    pay_type = models.CharField(max_length=255, verbose_name='支付方式')
    order_type = models.CharField(max_length=255, verbose_name='订单分类')
    express_type = models.CharField(max_length=255, verbose_name='物流公司')
    date_order = models.DateTimeField(default=timezone.now, verbose_name='下单时间')


class CustomerPcbOrderCost(models.Model):
    class Meta:
        db_table = 't_customer_pcb_order_cost_info'
        verbose_name = '客户PCB订单费用表'

    id = models.CharField(max_length=255, primary_key=True)
    pcb_number_order = models.CharField(max_length=255, verbose_name='订单编号')
    pcb_order_id = models.CharField(max_length=255, verbose_name='订单ID')
    # PCB 订单 费用明细
    engineering_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='工程费')
    imposition_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='拼版费')
    spray_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='喷镀费')
    board_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='板费')
    test_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='测试费')
    film_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='菲林费')
    urgent_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='加急费')
    color_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='颜色费')
    large_board_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='大板费')
    tax_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='税费')
    express_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='快递费')

    steel_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='钢网费')
    steel_express_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='钢网运费')


