from django.db import models
from system.models import Advertiser
from .conversion_group import ConversionGroup


class TargetGroupConversion(models.Model):
    class Meta:
        verbose_name_plural = "MTA Target Group Conversion"
    target = models.CharField(max_length=200)
    date_start = models.DateTimeField(null=False)
    date_end = models.DateTimeField(null=False)
    advertiser = models.ForeignKey(
        Advertiser, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(
        ConversionGroup, on_delete=models.CASCADE, null=True)
