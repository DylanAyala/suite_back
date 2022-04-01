from django.db import models 
from system.models import Advertiser, Campaign, Channel


class CoalitionsMetrics(models.Model):

    class Meta:
        verbose_name_plural = "MTA CoalitionsMetrics"

    date = models.DateTimeField(blank=False, editable=True, help_text="Date")
    advertiser = models.ForeignKey(Advertiser, related_name='MTACoalitionsMetrics_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='MTACoalitionsMetrics_Campaign', on_delete=models.CASCADE, null=True)
    channel = models.ForeignKey(
        Channel, related_name='MTACoalitionsMetrics_chanel', on_delete=models.CASCADE, null=True)
    coalitions = models.CharField(max_length=200)
    len_coalitions = models.IntegerField(default=0, help_text="Len Coalitions")
    total_paths = models.FloatField(default=0, blank=True, help_text="total")
    conversion_paths = models.FloatField(
        default=0, blank=True, help_text="conversion_paths")
    conversion_rate = models.FloatField(
        default=0, blank=True, help_text="conversion_rate")
    channel_attribution = models.FloatField(
        default=0, blank=True, help_text="channel_attribution")
