from django.db import models


class HotsModel(models.Model):
    title = models.CharField(verbose_name='热点标题', max_length=255)
    detail_url = models.CharField(verbose_name='详情页URL', max_length=255)
    source = models.IntegerField(verbose_name='数据来源',default=1)

    def __str__(self):
        return self.title

