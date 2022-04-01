from django.db import models 
from system.models import Advertiser, Campaign


class Irma(models.Model):

    class Meta:
        verbose_name_plural = "MTA Irma"

    date = models.DateTimeField(blank=False, editable=True, help_text="Date")
    advertiser = models.ForeignKey(Advertiser, related_name='MTAIrma_Advertiser',
                                   on_delete=models.CASCADE,
                                   null=True)
    campaign = models.ForeignKey(
        Campaign, related_name='MTAIrma_Campaign', on_delete=models.CASCADE, null=True)
    len_coalitions = models.IntegerField(default=0, help_text="Len coalitions")
    coalitions = models.FloatField(
        default=0, blank=True, help_text="coalitions")
    conversion_volume = models.FloatField(
        default=0, blank=True, help_text="conversion_volume")
    conversion_percentage = models.FloatField(
        default=0, blank=True, help_text="conversion_percentage")
    possible_truncation = models.FloatField(
        default=0, blank=True, help_text="Possible truncation")
    zero_percentage = models.FloatField(default=0, help_text="zero_percentage")
    zero_ten_percentage = models.FloatField(
        default=0, help_text="zero_ten_percentage")
    ten_twenty_percentage = models.FloatField(
        default=0, help_text="ten_twenty_percentage")
    twenty_thirty_percentage = models.FloatField(
        default=0, help_text="twenty_thirty_percentage")
    thirty_fourty_percentage = models.FloatField(
        default=0, help_text="thirty_fourty_percentage")
    fourty_fifty_percentage = models.FloatField(
        default=0, help_text="fourty_fifty_percentage")
    fifty_sixty_percentage = models.FloatField(
        default=0, help_text="fifty_sixty_percentage")
    sixty_seventy_percentage = models.FloatField(
        default=0, help_text="sixty_seventy_percentage")
    seventy_eighty_percentage = models.FloatField(
        default=0, help_text="seventy_eighty_percentage")
    eighty_ninety_percentage = models.FloatField(
        default=0, help_text="eighty_ninety_percentage")
    ninety_onehundred_percentage = models.FloatField(
        default=0, help_text="ninety_onehundred_percentage")
    one_hundred_percentage = models.FloatField(
        default=0, help_text="one_hundred_percentage")
    total = models.FloatField(default=0, help_text="total")
