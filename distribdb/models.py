from django.db import models
from datetime import datetime


class hardlock_keys(models.Model):

    port_name = (
        ('USB', 'USB'),
        ('LPT', 'LPT')
    )

    Mark                    = models.CharField(max_length=50, blank=True)
    ChipNo                  = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Номером чипа')
    Subcode                 = models.IntegerField(blank=True)
    ModAddr                 = models.IntegerField()
    Port                    = models.CharField(max_length=50, blank=False, default=None, choices=port_name)
    Free                    = models.BooleanField(default=False)
    Notes                   = models.TextField(max_length=8000, blank=True)

    class Meta:
        verbose_name = 'Ключ аппаратной защиты (Hardlock)'
        ordering = ('ChipNo',)


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

    ChipNo                  = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Номером чипа')
    Free                    = models.BooleanField(default=False)
    Port                    = models.CharField(max_length=50, blank=False, default=None, choices=port_name)
    Type                    = models.CharField(max_length=50, blank=False, default=None, choices=type_key)
    TimeLimit               = models.DateField(null=True, blank=True)
    Licenses                = models.CharField(max_length=255, blank=True)
    Notes                   = models.TextField(max_length=8000, blank=True)

    class Meta:
        verbose_name = 'Ключ аппаратной защиты (HASP)'
        ordering = ('ChipNo',)


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


class Lang_types(models.Model):

    Lang                    = models.CharField(max_length=50, blank=False)
    LCode                   = models.IntegerField()
    ISDefine                = models.CharField(max_length=50, blank=False)


class OS_type(models.Model):

    OS                      = models.CharField(max_length=50, blank=False)
    OSCode                  = models.IntegerField(blank=False)


class executables(models.Model):

    FileName                = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Именем файла')

    def __str__(self):
        return self.FileName

    class Meta:
        verbose_name = 'Исполняемый модуль'
        ordering = ('FileName',)


class FASModules(models.Model):

    ExecutableID            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, default=id(1))
    FASNo                   = models.IntegerField(blank=False, unique=True, verbose_name='FAS номером')

    class Meta:
        verbose_name = 'FAS модуль'
        ordering = ('ExecutableID',)


class ExecutablePaths(models.Model):

    ExecutableID            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, default=id(1))
    ISPath                  = models.CharField(max_length=250, blank=False)
    Source                  = models.CharField(max_length=800, blank=True)
    Dest                    = models.CharField(max_length=800, blank=True)

    class Meta:
        ordering = ('ExecutableID',)


class RegSystems(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=50, blank=False)
    Hide                    = models.BooleanField(default=False)
    Description             = models.TextField(max_length=8000, blank=True)

    class Meta:
        ordering = ('UserName',)

    def __str__(self):
        return self.UserName


class TypeRegsys(models.Model):

    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='Тип ЛА')
    RegsysID                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='Система регистрации')
    ISPath                  = models.CharField(max_length=255, blank=False)
    UserNameRegsys          = models.CharField(max_length=36, blank=False)
    SysNameRegsys           = models.CharField(max_length=16, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.RegsysID.UserName

    class Meta:
        ordering = ('TypeID',)
        unique_together = ('TypeID', 'RegsysID')
        verbose_name = 'Система регистрации по типам ЛА'


class Tasks(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Системным именем')
    UserName                = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.SysName

    class Meta:
        verbose_name = 'База экспрессов'
        ordering = ('SysName',)


class TypeTasks(models.Model):

    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='Тип ЛА')
    TaskID                  = models.ForeignKey('Tasks', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='База экспресса')
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.TaskID.UserName

    class Meta:
        verbose_name = 'Экспресс для типов ЛА'
        unique_together = ('TypeID', 'TaskID')


class Misc(models.Model):

    Name                    = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Названием')
    SysName                 = models.CharField(max_length=50, blank=True)
    UserName                = models.CharField(max_length=50, blank=True)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Допольнительный элемент ЛА'
        ordering = ('Name',)


class TypeMisc(models.Model):

    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='Тип ЛА')
    MiscID                  = models.ForeignKey('Misc', on_delete=models.CASCADE, blank=False, default=id(1), verbose_name='Элемент')
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.MiscID.Name

    class Meta:
        verbose_name = 'Дополнительный элемент ЛА'
        unique_together = ('TypeID', 'MiscID')
        ordering = ('TypeID',)


class Organisations(models.Model):

    Name                    = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Названием')
    City                    = models.CharField(max_length=50, blank=True)
    Notes                   = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Организация'
        ordering = ('Name',)


class drop_device(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Пользовательским именем')
    ISPath                  = models.CharField(max_length=250, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.UserName

    class Meta:
        verbose_name = 'Устройство сброса'
        ordering = ('SysName',)


class RegSysDevices(models.Model):

    RegsysID                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, default=id(1))
    DeviceID                = models.ForeignKey('drop_device', on_delete=models.CASCADE, blank=False, default=id(1))

    def __str__(self):
        return '%s %s' % (self.RegsysID.UserName, self.DeviceID.UserName)

    class Meta:
        ordering = ('RegsysID',)


class Modules(models.Model):

    Name                    = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Названием')
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Дополнительный модуль ПО'
        ordering = ('Name',)


class Drivers(models.Model):

    Name                    = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Названием')
    Xno                     = models.IntegerField(blank=False)
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Драйвер'
        ordering = ('Name',)


class Sets(models.Model):

    UserFriendlyID          = models.BigAutoField(primary_key=True)
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)
    Regsys                  = models.ManyToManyField('TypeRegsys')
    TypeTasks               = models.ManyToManyField('TypeTasks')
    TypeMisc                = models.ManyToManyField('TypeMisc')
    Modules                 = models.ManyToManyField('Modules', blank=True)
    RegSysDevices           = models.ManyToManyField('RegSystems')
    Devices                 = models.ManyToManyField('drop_device', blank=True)
    Drivers                 = models.ManyToManyField('Drivers', blank=True)

    def __str__(self):
        return '%s %s' % (self.Regsys, self.TypeTasks)

    class Meta:
        ordering = ('-UserFriendlyID',)