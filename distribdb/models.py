from django.db import models
from datetime import datetime


class drop_device(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=250, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    class Meta:
        ordering = ('UserName',)

    def __str__(self):
        return self.UserName


class hasp_keys(models.Model):

    port_name = (
        ('USB', 'USB'),
        ('LPT', 'LPT')
    )

    type_key = (
        ('LocalHASP', 'LocalHASP'),
        ('TimeHASP', 'TimeHASP'),
        ('NetHASP', 'NetHasp')
    )

    ChipNo                  = models.CharField(max_length=50, blank=False, unique=True)
    Free                    = models.BooleanField(default=False)
    Port                    = models.CharField(max_length=50, blank=False, default=None, choices=port_name)
    Type                    = models.CharField(max_length=50, blank=False, default=None, choices=type_key)
    TimeLimit               = models.DateField(null=True, blank=True)
    Licenses                = models.CharField(max_length=255, blank=True)
    Notes                   = models.TextField(max_length=8000, blank=True)


class hardlock_keys(models.Model):

    port_name = (
        ('USB', 'USB'),
        ('LPT', 'LPT')
    )

    Mark                    = models.CharField(max_length=50, blank=True)
    ChipNo                  = models.CharField(max_length=50, blank=False)
    Subcode                 = models.IntegerField(blank=True)
    ModAddr                 = models.IntegerField()
    Port                    = models.CharField(max_length=50, blank=False, default=None, choices=port_name)
    Free                    = models.BooleanField(default=False)
    Notes                   = models.TextField(max_length=8000, blank=True)


class Lang_types(models.Model):

    Lang                    = models.CharField(max_length=50, blank=False)
    LCode                   = models.IntegerField()
    ISDefine                = models.CharField(max_length=50, blank=False)


class OS_type(models.Model):

    OS                      = models.CharField(max_length=50, blank=False)
    OSCode                  = models.IntegerField(blank=False)


class executables(models.Model):

    FileName                = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.FileName

    class Meta:
        ordering = ('FileName',)


class FASModules(models.Model):

    ExecutableID            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, default=id(1))
    FASNo                   = models.IntegerField(blank=False)


class ExecutablePaths(models.Model):

    ExecutableID            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, default=id(1))
    ISPath                  = models.CharField(max_length=250, blank=False)
    Source                  = models.CharField(max_length=800, blank=False)
    Dest                    = models.CharField(max_length=800, blank=False)


class RegSystems(models.Model):

    SysName                 = models.CharField(max_length=50, blank=True)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=50, blank=True)
    Hide                    = models.BooleanField(default=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.UserName

    class Meta:
        ordering = ('UserName',)


class Tasks(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False, unique=True)
    UserName                = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.SysName

    class Meta:
        ordering = ('SysName',)


class TypeTasks(models.Model):

    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, default=id(1))
    TaskID                  = models.ForeignKey('Tasks', on_delete=models.CASCADE, blank=False, default=id(1))
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.TaskID.UserName

    class Meta:
        verbose_name = 'Экспресс для типов ЛА'
        unique_together = ('TypeID', 'TaskID')


class Misc(models.Model):

    Name                    = models.CharField(max_length=255, blank=False)
    SysName                 = models.CharField(max_length=50, blank=True)
    UserName                = models.CharField(max_length=50, blank=True)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('Name',)


class TypeMisc(models.Model):

    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, default=id(1))
    MiscID                  = models.ForeignKey('Misc', on_delete=models.CASCADE, blank=False, default=id(1))
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.MiscID.Name


class Organisations(models.Model):

    Name                    = models.CharField(max_length=50, blank=True)
    City                    = models.CharField(max_length=50, blank=True)
    Notes                   = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('Name',)


class RegSysDevices(models.Model):

    RegsysID                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, default=id(1))
    DeviceID                = models.ForeignKey('drop_device', on_delete=models.CASCADE, blank=False, default=id(1))

    def __str__(self):
        return '%s %s' % (self.RegsysID.UserName, self.DeviceID.UserName)


class Modules(models.Model):

    Name                    = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)
    ISPath                  = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('Name',)


class Drivers(models.Model):

    Name                    = models.CharField(max_length=50, blank=False)
    Xno                     = models.IntegerField(blank=False)
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)


class Plane_types(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=250, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.UserName

    class Meta:
        ordering = ('UserName',)
        verbose_name = 'Типы ЛА'


class TypeRegsys(models.Model):

    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='"Тип ЛА"')
    RegsysID                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='"Система регистрации"')
    ISPath                  = models.CharField(max_length=255, blank=False)
    UserNameRegsys          = models.CharField(max_length=36, blank=False)
    SysNameRegsys           = models.CharField(max_length=16, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.RegsysID.UserName

    class Meta:
        ordering = ('TypeID',)
        unique_together = ('TypeID', 'RegsysID')
        verbose_name = '"Система регистрации по типам ЛА"'


class Sets(models.Model):

    UserFriendlyID          = models.BigAutoField(primary_key=True)
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)
    RegsysID                = models.ManyToManyField('TypeRegsys')
    TypeTasksID             = models.ManyToManyField('TypeTasks')
    TypeMiscID              = models.ManyToManyField('TypeMisc')
    RegSysDevicesID         = models.ManyToManyField('RegSystems')
    SetModulesID            = models.ManyToManyField('Modules')

    def __str__(self):
        return '%s %s' % (self.RegsysID, self.TypeTasksID)
