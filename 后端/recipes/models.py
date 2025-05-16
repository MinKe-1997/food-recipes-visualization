from django.db import models


# Create your models here.

class Menu(models.Model):
    id = models.CharField('唯一标识符', primary_key=True, max_length=36)
    big_type = models.CharField('大类型', max_length=32, blank=True, null=True)
    type = models.CharField('类型', max_length=32, blank=True, null=True)
    name = models.CharField('名称', max_length=32, blank=True, null=True)
    img = models.CharField('图片链接', max_length=255, blank=True, null=True)
    peiliao = models.CharField('配料', max_length=255, blank=True, null=True)
    zz = models.CharField('制作步骤', max_length=25, blank=True, null=True)
    imgze = models.CharField('制作步骤图片链接', max_length=255, blank=True, null=True)
    url = models.CharField('链接', max_length=255, blank=True, null=True)
    sc = models.CharField('食材', max_length=36, blank=True, null=True)
    cat = models.CharField('分类', max_length=32, blank=True, null=True)
    num = models.CharField('数量', max_length=3, blank=True, null=True)

    class Meta:
        db_table = "menu"
        verbose_name_plural = "美食管理"
        verbose_name = "美食管理"


class User(models.Model):
    id = models.CharField(verbose_name='用户ID', primary_key=True, max_length=31)
    name = models.CharField(verbose_name='用户名', max_length=32, blank=True, null=True)
    password = models.CharField(verbose_name='密码', max_length=32, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'user'
        verbose_name_plural = '用户'
        verbose_name = '用户'
