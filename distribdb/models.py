from django.db import models
from datetime import datetime
import uuid


class hardlock_keys(models.Model):

    port_name = (
        ('USB', 'USB'),
        ('LPT', 'LPT')
    )
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mark                    = models.CharField(max_length=50, blank=True)
    chipno                  = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Номером чипа')
    subcode                 = models.IntegerField(blank=True)
    modaddr                 = models.IntegerField()
    port                    = models.CharField(max_length=50, blank=False, default=None, choices=port_name)
    free                    = models.BooleanField(default=False)
    notes                   = models.TextField(max_length=8000, blank=True)

    class Meta:
        verbose_name = 'Ключ аппаратной защиты (Hardlock)'
        ordering = ('chipno',)
        db_table = 'hl_keys'


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

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chipno                  = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Номером чипа')
    free                    = models.BooleanField(default=False)
    port                    = models.CharField(max_length=50, blank=False, default=None, choices=port_name)
    type                    = models.CharField(max_length=50, blank=False, default=None, choices=type_key)
    timelimit               = models.DateField(null=True, blank=True)
    licenses                = models.CharField(max_length=255, blank=True)
    notes                   = models.TextField(max_length=8000, blank=True)

    class Meta:
        verbose_name = 'Ключ аппаратной защиты (HASP)'
        ordering = ('chipno',)
        db_table = 'hasp_keys'


class Plane_types(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sysname                 = models.CharField(max_length=50, blank=False)
    username                = models.CharField(max_length=50, blank=False)
    ispath                  = models.CharField(max_length=250, blank=False)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
        verbose_name = 'Типы ЛА'
        db_table = 'planetypes'



class Lang_types(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lang                    = models.CharField(max_length=50, blank=False)
    lcode                   = models.IntegerField()
    isdefine                = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'lang'


class OS_type(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    os                      = models.CharField(max_length=50, blank=False)
    oscode                  = models.IntegerField(blank=False)

    class Meta:
        db_table = 'os'


class executables(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename                = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Именем файла')

    def __str__(self):
        return self.filename

    class Meta:
        verbose_name = 'Исполняемый модуль'
        ordering = ('filename',)
        db_table = 'executables'


class FASModules(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    executableid            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False)
    fasno                   = models.IntegerField(blank=False, unique=True, verbose_name='FAS номером')

    class Meta:
        verbose_name = 'FAS модуль'
        ordering = ('executableid',)
        db_table = 'fasmodules'


class ExecutablePaths(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    executableid            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False)
    ispath                  = models.CharField(max_length=250, blank=False)
    source                  = models.CharField(max_length=800, blank=True)
    dest                    = models.CharField(max_length=800, blank=True)

    class Meta:
        ordering = ('executableid',)
        db_table = 'executablepaths'


class RegSystems(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sysname                 = models.CharField(max_length=50, blank=False)
    username                = models.CharField(max_length=50, blank=False)
    ispath                  = models.CharField(max_length=50, blank=False)
    hide                    = models.BooleanField(default=False)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
        db_table = 'regsystems'


class TypeRegsys(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typeid                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА')
    regsysid                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, verbose_name='Система регистрации')
    ispath                  = models.CharField(max_length=255, blank=False)
    usernameregsys          = models.CharField(max_length=36, blank=False)
    sysnameregsys           = models.CharField(max_length=16, blank=False)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.regsysid.username

    class Meta:
        ordering = ('typeid',)
        unique_together = ('typeid', 'regsysid')
        verbose_name = 'Система регистрации по типам ЛА'
        db_table = 'typeregsys'


class Tasks(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sysname                 = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Системным именем')
    username                = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.sysname

    class Meta:
        verbose_name = 'База экспрессов'
        ordering = ('sysname',)
        db_table = 'tasks'


class TypeTasks(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typeid                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА')
    taskid                  = models.ForeignKey('Tasks', on_delete=models.CASCADE, blank=False, verbose_name='База экспресса')
    ispath                  = models.CharField(max_length=255, blank=False)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.taskid.sysname

    class Meta:
        ordering = ('typeid',)
        verbose_name = 'Экспресс для типов ЛА'
        unique_together = ('typeid', 'taskid')
        db_table = 'typetasks'


class Misc(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                    = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Названием')
    sysname                 = models.CharField(max_length=50, blank=True)
    username                = models.CharField(max_length=50, blank=True)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Допольнительный элемент ЛА'
        ordering = ('name',)
        db_table = 'misc'


class TypeMisc(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typeid                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА')
    miscid                  = models.ForeignKey('Misc', on_delete=models.CASCADE, blank=False, verbose_name='Элемент')
    ispath                  = models.CharField(max_length=255, blank=False)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.miscid.name

    class Meta:
        verbose_name = 'Дополнительный элемент ЛА'
        unique_together = ('typeid', 'miscid')
        ordering = ('typeid',)
        db_table = 'typemisc'


class Organisations(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                    = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Названием')
    city                    = models.CharField(max_length=50, blank=True)
    notes                   = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        ordering = ('name',)
        db_table = 'organisations'


class drop_device(models.Model):

    id                       = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sysname                 = models.CharField(max_length=50, blank=False)
    username                = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Пользовательским именем')
    ispath                   = models.CharField(max_length=250, blank=False)
    description              = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.sysname

    class Meta:
        verbose_name = 'Устройство сброса'
        ordering = ('sysname',)
        db_table = 'devices'


class RegSysDevices(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    regsysid                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False)
    deviceid                = models.ForeignKey('drop_device', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return '%s %s' % (self.regsysid.username, self.deviceid.username)

    class Meta:
        ordering = ('regsysid',)
        db_table = 'regsysdevices'


class Modules(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                    = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Названием')
    ispath                  = models.CharField(max_length=255, blank=False)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дополнительный модуль ПО'
        ordering = ('name',)
        db_table = 'modules'


class Drivers(models.Model):

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                    = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Названием')
    xno                     = models.IntegerField(blank=False)
    ispath                  = models.CharField(max_length=255, blank=False)
    description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Драйвер'
        ordering = ('name',)
        db_table = 'drivers'


class Sets(models.Model):

    UserFriendlyID          = models.BigAutoField(primary_key=True)
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)
    Regsys                  = models.ManyToManyField('TypeRegsys')
    TypeTasks               = models.ManyToManyField('TypeTasks')
    TypeMisc                = models.ManyToManyField('TypeMisc')
    Modules                 = models.ManyToManyField('Modules', blank=True)
    RegSysDevices           = models.ManyToManyField('RegSystems', blank=True)
    Devices                 = models.ManyToManyField('drop_device', blank=True)
    Drivers                 = models.ManyToManyField('Drivers', blank=True)

    def __str__(self):
        return '%s %s' % (self.Regsys, self.TypeTasks)

    class Meta:
        ordering = ('-UserFriendlyID',)