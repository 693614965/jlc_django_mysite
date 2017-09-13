from django.db import models


class CustomerPcbDataInfo(models.Model):
    class Meta:
        db_table = 't_customer_pcb_data_info'
        verbose_name = '客户PCB资料信息表'

    id = models.CharField(max_length=255, primary_key=True)
    layer = models.IntegerField(verbose_name='层数')
    width = models.IntegerField(verbose_name='宽度')
    length = models.IntegerField(verbose_name='长度')
    board_area = models.IntegerField(verbose_name='板子面积')
    pcb_num = models.IntegerField(verbose_name='板子数量')
    thickness = models.FloatField(verbose_name='厚度')
    solder_color = models.CharField(max_length=255, verbose_name='阻焊颜色')
    char_color = models.CharField(max_length=255, verbose_name='字符颜色')
    pad_cover = models.CharField(max_length=255, verbose_name='焊盘覆盖')
    pad_spraying = models.CharField(max_length=255, verbose_name='焊盘喷镀')
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
    status = models.IntegerField(verbose_name='状态', default=0)
    pcb_file_name = models.CharField(max_length=255, verbose_name='pcb文件名称')
    pcb_file_url = models.CharField(max_length=255, verbose_name='pcb文件保存磁盘地址')
    customer_id = models.CharField(max_length=255, verbose_name='客户ID')
