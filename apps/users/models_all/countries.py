from django.db import models


class Countries(models.Model):

    class Meta:
        verbose_name_plural = "Countries"

    iso_code = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
