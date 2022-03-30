from django.contrib import admin
from .models import ConversionGroup, ConversionType, TargetGroupConversion, MtaResult, PathsMetrics


admin.site.register(ConversionGroup)
admin.site.register(ConversionType)
admin.site.register(TargetGroupConversion)
admin.site.register(MtaResult)
admin.site.register(PathsMetrics)
