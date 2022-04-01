from distutils.command.build_scripts import first_line_re
from django.db import models 
from system.models import Advertiser, Campaign


class PathsMetrics(models.Model):

    class Meta:
        verbose_name_plural = "MTA Paths Metrics"

    date = models.DateTimeField(blank=False, editable=True, help_text="Date")
    advertiser = models.ForeignKey(Advertiser, related_name='MTAPathsMetrics_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='MTAPathsMetrics_Campaign', on_delete=models.CASCADE, null=True)
    total_paths = models.FloatField(
        default=0, blank=True, help_text="total_paths")
