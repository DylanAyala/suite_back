from django.db import models 
from .advertaiser import Advertiser


class Channel(models.Model):

    class Meta:
        verbose_name_plural = "System Channel"

    name = models.CharField(max_length=50)
    advertiser = models.ForeignKey(Advertiser, related_name='Channel_Advertiser', on_delete=models.CASCADE,
                                   null=True)

    def __str__(self):
        return self.name
