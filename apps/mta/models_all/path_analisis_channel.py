from django.db import models
from system.models import Campaign, Advertiser


class PathAnalisisChannel(models.Model):

    class Meta:
        verbose_name_plural = "MTA Path Analisis Channels"

    date = models.DateTimeField(blank=False, editable=True, help_text="Date")
    advertiser = models.ForeignKey(Advertiser, related_name='MTAPathAnalisisChannels_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='MTAPathAnalisisChannels_Campaign', on_delete=models.CASCADE, null=True)
    conversion_type = models.ForeignKey('ConversionType', related_name='MtaPathAnalisisChannels_conversionType',
                                        on_delete=models.CASCADE, null=True)
    channels_quantity = models.FloatField(
        default=0, blank=True, help_text="total_paths")
    paths_count = models.FloatField(
        default=0, blank=True, help_text="total_paths")
