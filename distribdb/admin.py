from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.drop_device)
admin.site.register(models.hasp_keys)
admin.site.register(models.hardlock_keys)
admin.site.register(models.Lang_types)
admin.site.register(models.OS_type)