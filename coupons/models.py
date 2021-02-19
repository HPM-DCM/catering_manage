from django.db import models
class Coupon(models.Model):
    username=models.CharField(max_length=200,verbose_name='用户名')
    money=models.CharField(max_length=10,verbose_name='面值')
    name=models.CharField(max_length=20,verbose_name='标题')
    condition=models.CharField(max_length=200,verbose_name='miaos ')
    effective_start=models.CharField(max_length=20,verbose_name='开始时间')
    effective_end=models.CharField(max_length=20,verbose_name='失效时间')