from django.db import models 
from system.models import Advertiser, Campaign, Channel
from .conversion_type import ConversionType
from django.db import models  as moD

class MtaResult(models.Model):
    class Meta:
        verbose_name_plural = "MTA Result"

    advertiser = models.ForeignKey(Advertiser, related_name='MtaResult_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='MtaResult_Campaign', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(
        blank=False, editable=True, help_text="Date", db_index=True)
    conversion_type = models.ForeignKey(
        ConversionType, related_name='MtaResult_conversionType', on_delete=models.CASCADE, null=True)
    channel = models.ForeignKey(
        Channel, related_name='MtaResult_chanel', on_delete=models.CASCADE, null=True)
    revenue_shapley = models.FloatField(
        default=0, blank=True, help_text="Revenue shapley")
    atributed_conversion_shapley = models.FloatField(
        default=0, blank=True, help_text="Atributed Conversion Shapley")
    atributed_conversiones_lineal = models.FloatField(
        default=0, blank=True, help_text="Atributed Conversiones Lineal")
    revenue_linear = models.FloatField(
        default=0, blank=True, help_text="Revenue Linear")
    revenue_first_click = models.FloatField(
        default=0, blank=True, help_text="Revenue_Frst Click")
    revenue_last_click = models.FloatField(
        default=0, blank=True, help_text="Revenue Last Click")
    stimuli_quantity_paths = models.FloatField(
        default=0, blank=True, help_text="Stimuli Quantity Paths")
    paths_quantity = models.FloatField(
        default=0, blank=True, help_text="Paths Quantity")
    assistances_role = models.FloatField(
        default=0, blank=True, help_text="Rol assistances (of the paths ending today)")
    conversion_role = models.FloatField(
        default=0, blank=True, help_text="Role conversion (of the paths ending today)")
    acquisition_role = models.FloatField(
        default=0, blank=True, help_text="Acquisition role(of the paths ending today)")
    shapley = models.FloatField(default=0, blank=True, help_text="Shapley")
    this_type_conversions = models.FloatField(
        default=0, blank=True, help_text="This type conversions")
    convertion_paths_with_this_channel = models.FloatField(
        default=0, blank=True, help_text="Convertion paths with this channel")
    daily_impulses = models.FloatField(
        default=0, blank=True, help_text="Daily impulses")
    campaign_mta = models.CharField(max_length=300, default='', db_index=True)
    source = models.CharField(max_length=100, default='', db_index=True)
    content = models.CharField(max_length=300, default='', db_index=True)
