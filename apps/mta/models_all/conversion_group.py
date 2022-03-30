from django.db import models
from system.models import Advertiser


class ConversionGroup(models.Model):
    class Meta:
        verbose_name_plural = "MTA ConversionGroup"
    group = models.CharField(max_length=100)
    advertiser = models.ForeignKey(Advertiser, related_name='ConversionGroup_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)

    def __str__(self):
        return self.group
