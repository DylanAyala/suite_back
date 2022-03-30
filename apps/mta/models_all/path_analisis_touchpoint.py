from django.db import models
from system.models import Campaign, Advertiser


class PathAnalisisTouchpoint(models.Model):

    class Meta:
        verbose_name_plural = "MTA Path Analisis Touchpoint"

    date = models.DateTimeField(blank=False, editable=True, help_text="Date")
    advertiser = models.ForeignKey(Advertiser, related_name='MTAPathAnalisisTouchpoint_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='MTAPathAnalisisTouchpoint_Campaign', on_delete=models.CASCADE, null=True)
    conversion_type = models.ForeignKey('ConversionType', related_name='MtaPathAnalisisTouchpoint_conversionType',
                                        on_delete=models.CASCADE, null=True)
    touchpoints_quantity = models.FloatField(
        default=0, blank=True, help_text="total_paths")
    paths_count = models.FloatField(
        default=0, blank=True, help_text="total_paths")
