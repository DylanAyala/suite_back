from django.db import models 
from .advertaiser import Advertiser
from .modules import Module


class Campaign(models.Model):

    class Meta:
        verbose_name_plural = "System Campaign"

    """Type user Campaign"""
    name = models.CharField(max_length=50, blank=True)
    advertiser = models.ForeignKey(Advertiser, related_name='Campaign_Advertiser', on_delete=models.CASCADE,
                                   null=True)
    module = models.ManyToManyField(
        Module, related_name='Campaign_Advertiser_module', blank=True)
    campaign_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
