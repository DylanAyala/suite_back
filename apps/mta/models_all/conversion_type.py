from django.db import models
from system.models import Advertiser, Campaign
from .conversion_group import ConversionGroup


class ConversionType(models.Model):

    class Meta:
        verbose_name_plural = "MTA ConversionType"
    id = models.AutoField(primary_key=True, help_text="Unique id")
    advertiser = models.ForeignKey(Advertiser, related_name='ConversionType_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='ConversionType_Campaign', on_delete=models.CASCADE, null=True)
    conversion_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    group = models.ForeignKey(ConversionGroup, on_delete=models.CASCADE,
                              null=True)
