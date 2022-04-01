from django.db import models 
from suite_back import settings
from users.models import Countries


class Advertiser(models.Model):

    class Meta:
        verbose_name_plural = "System Advertiser"

    id = models.AutoField(primary_key=True, help_text="Unique id")
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    countries = models.ForeignKey(Countries, related_name='Advertiser_Countries', on_delete=models.CASCADE,
                                  null=True, default=1)
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        #self.category = self.hero.category
        super().save(*args, **kwargs)
