from django.db import models 
import datetime
from system.models import Advertiser, Campaign, Channel


class Investment(models.Model):

    class Meta:
        verbose_name_plural = "MTA Invesment"

    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    advertiser = models.ForeignKey(Advertiser, related_name='MtaInvesment_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='MTAInvesment_Campaign', on_delete=models.CASCADE, null=True)
    channel = models.ForeignKey(
        Channel, related_name='MTAInvesment_chanel', on_delete=models.CASCADE, null=True)
    invesment = models.FloatField(default=0, blank=True, help_text="invesment")
    campaign_mta = models.CharField(max_length=300, default='')
    source = models.CharField(max_length=100, default='')
    content = models.CharField(max_length=300, default='')
