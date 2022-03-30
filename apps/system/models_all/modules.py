from django.db import models
from users.models import Countries


class Module(models.Model):

    class Meta:
        verbose_name_plural = "System Module"

    id = models.AutoField(primary_key=True, help_text="Unique id")
    name = models.CharField(max_length=50, blank=True)
    menu = models.CharField(max_length=50, blank=True)
    country = models.ManyToManyField(
        Countries, related_name='system_module_countries', blank=True)

    def __str__(self):
        return self.name
