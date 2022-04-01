from django.db import models 
from system.models import Advertiser


class CampaingType(models.Model):
    class Meta:
        verbose_name_plural = "MTA Campaign Type"

    name = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    advertiser = models.ForeignKey(Advertiser, related_name='CampaingType_advertiser',
                                   on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
