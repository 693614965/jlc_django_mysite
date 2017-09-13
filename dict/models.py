from django.db import models


class DictModel(models.Model):
    class Meta:
        db_table = 't_dict'
        verbose_name = '系统字典表'

    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称')
    code = models.CharField(max_length=50, verbose_name='编码')
    serial = models.IntegerField(verbose_name='序号')


class DictDetailModel(models.Model):
    class Meta:
        db_table = 't_dict_detail'
        verbose_name = '系统字典明细表'

    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称')
    code = models.CharField(max_length=50, verbose_name='编码')
    serial = models.IntegerField(verbose_name='序号')
    dictId = models.CharField(max_length=50, verbose_name='字典业务外键ID')
