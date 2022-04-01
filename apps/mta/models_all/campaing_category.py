from django.db import models 
from system.models import Advertiser


class CampaingCategory(models.Model):
    class Meta:
        verbose_name_plural = "MTA Campaign Category"

    name = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    sub = models.BooleanField(default=False)
    advertiser = models.ForeignKey(Advertiser, related_name='CampaingCategory_advertiser',
                                   on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
