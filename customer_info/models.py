from django.db import models
from django.utils import timezone


class CustomerInfo(models.Model):
    class Meta:
        db_table = 't_customer_info'
        verbose_name = '客户信息表'

    id = models.CharField(max_length=255, primary_key=True)
    code = models.CharField(max_length=255, verbose_name='客户编码')
    name = models.CharField(max_length=255, verbose_name='客户姓名')
    age = models.IntegerField(verbose_name='年龄')
    mobile = models.CharField(max_length=255, verbose_name='客户手机')
    home_address = models.CharField(max_length=255, verbose_name='客户家庭住址')
    work_unit = models.CharField(max_length=255, verbose_name='客户工作单位')
    education = models.CharField(max_length=255, verbose_name='客户学历')
    email = models.CharField(max_length=255, verbose_name='客户邮箱')
    qq = models.CharField(max_length=255, verbose_name='客户QQ')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='客户注册时间')
    user_id = models.CharField(max_length=255, verbose_name='系统用户ID')


