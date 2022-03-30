from django.contrib import admin
from .models import Module, Advertiser, ConfigruationAdvertiser, Channel, Campaign

# Register your models here.

admin.site.register(Module)
admin.site.register(Advertiser)
admin.site.register(ConfigruationAdvertiser)
admin.site.register(Campaign)
admin.site.register(Channel)