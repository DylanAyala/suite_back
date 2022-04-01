from django.contrib import admin
from .models import ConversionGroup, ConversionType, TargetGroupConversion, MtaResult, PathsMetrics, \
    PathAnalisisTouchpoint, PathAnalisisChannel, Irma, Investment, CoalitionsMetrics, CampaingType, CampaingCategory


admin.site.register(ConversionGroup)
admin.site.register(ConversionType)
admin.site.register(TargetGroupConversion)
admin.site.register(MtaResult)
admin.site.register(PathsMetrics)
admin.site.register(PathAnalisisTouchpoint)
admin.site.register(PathAnalisisChannel)
admin.site.register(Irma)
admin.site.register(Investment)
admin.site.register(CoalitionsMetrics)
admin.site.register(CampaingType)
admin.site.register(CampaingCategory)
