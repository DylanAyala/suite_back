from django.db import models
import datetime
from .advertaiser import Advertiser


class ConfigruationAdvertiser(models.Model):

    class Meta:
        verbose_name_plural = "System Configuration Advertiser"

    enabled = models.BooleanField(default=False)
    advertiser = models.ForeignKey(Advertiser, related_name='ConfigurationAdvertiser_Advertiser', on_delete=models.CASCADE,
                                   null=True)
    name_configuration = models.CharField(max_length=100, blank=False)
    date_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    date_time_update = models.DateTimeField(
        default=datetime.datetime.now, blank=True)
    configuration = models.TextField(blank=False)

    @property
    def get_advertiser_name(self):
        return self.advertiser.name
