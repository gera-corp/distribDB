from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.drop_device)
admin.site.register(models.hasp_keys)
admin.site.register(models.hardlock_keys)
admin.site.register(models.Lang_types)
admin.site.register(models.OS_type)
admin.site.register(models.executables)
admin.site.register(models.FASModules)
admin.site.register(models.ExecutablePaths)
admin.site.register(models.RegSystems)
admin.site.register(models.TypeRegsys)
admin.site.register(models.Tasks)
admin.site.register(models.TypeTasks)
admin.site.register(models.Misc)
admin.site.register(models.TypeMisc)
admin.site.register(models.Organisations)
admin.site.register(models.RegSysDevices)
admin.site.register(models.Modules)
admin.site.register(models.Drivers)
admin.site.register(models.Sets)