from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(verbose_name='编号',primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=10)
    password = models.CharField(verbose_name="密码", max_length=10)
    info = models.TextField(verbose_name='个人说明', max_length=100)