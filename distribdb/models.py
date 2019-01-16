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
        verbose_name = 'Ключ аппаратной защиты (hardlock)'
        ordering = ('chipno',)
        db_table = 'hl_keys'

    def __str__(self):
        return self.chipno


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
    licenses                = models.CharField(max_length=255, blank=True, null=True)
    notes                   = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.chipno

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

    def __str__(self):
        return self.lang

    class Meta:
        db_table = 'lang'


class OS_type(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    os                      = models.CharField(max_length=50, blank=False)
    oscode                  = models.IntegerField(blank=False)

    def __str__(self):
        return self.os

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
    executableid            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, db_column='executableid')
    fasno                   = models.IntegerField(blank=False, unique=True, verbose_name='FAS номером')

    class Meta:
        verbose_name = 'FAS модуль'
        ordering = ('executableid',)
        db_table = 'fasmodules'


class ExecutablePaths(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    executableid            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, db_column='executableid')
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
        return '%s %s' % (self.username, self.hide)

    class Meta:
        ordering = ('username',)
        db_table = 'regsystems'


class TypeRegsys(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typeid                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА', db_column='typeid')
    regsysid                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, verbose_name='Система регистрации', db_column='regsysid')
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
    typeid                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА', db_column='typeid')
    taskid                  = models.ForeignKey('Tasks', on_delete=models.CASCADE, blank=False, verbose_name='База экспресса', db_column='taskid')
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
    typeid                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА', db_column='typeid')
    miscid                  = models.ForeignKey('Misc', on_delete=models.CASCADE, blank=False, verbose_name='Элемент', db_column='miscid')
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
    sysname                  = models.CharField(max_length=50, blank=False)
    username                 = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Пользовательским именем')
    ispath                   = models.CharField(max_length=250, blank=False)
    description              = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Устройство сброса'
        ordering = ('username',)
        db_table = 'devices'


class RegSysDevices(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    regsysid                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, db_column='regsysid')
    deviceid                = models.ForeignKey('drop_device', on_delete=models.CASCADE, blank=False, db_column='deviceid')

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


def ids():
    try:
        no = Sets.objects.first().userfriendlyid
        return no + 1
    except:
        return 1


class Sets(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userfriendlyid          = models.BigIntegerField(default=ids, unique=True, editable=False)
    date                    = models.DateField(null=False, blank=False, default=datetime.now)
    typeregsystems          = models.ManyToManyField('TypeRegsys', through='TypeRegSysRelationship', through_fields=('setid', 'typeregsysid'))
    typetasks               = models.ManyToManyField('TypeTasks', through='TypeTasksRelationship', through_fields=('setid', 'typetaskid'))
    typemisc                = models.ManyToManyField('TypeMisc', through='TypeMiscRelationship', through_fields=('setid', 'typemiscid'))
    modules                 = models.ManyToManyField('Modules', through='ModulesRelationship', through_fields=('setid', 'moduleid'), blank=True)
    regsystems              = models.ManyToManyField('RegSystems', through='RegSystemsRelationship', through_fields=('setid', 'regsysid'), blank=True)
    devices                 = models.ManyToManyField('drop_device', through='drop_deviceRelationship', through_fields=('setid', 'deviceid'), blank=True)
    drivers                 = models.ManyToManyField('Drivers', through='DriversRelationship', through_fields=('setid', 'driverid'), blank=True)

    def __str__(self):
        return '%s --- %s' % (self.date.strftime('%d.%m.%Y'), self.userfriendlyid)

    class Meta:
        ordering = ('-userfriendlyid',)
        db_table = 'sets'


class TypeRegSysRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='setid')
    typeregsysid              = models.ForeignKey('TypeRegsys', on_delete=models.CASCADE, db_column='typeregsysid')

    class Meta:
        ordering = ('typeregsysid',)
        db_table = 'settyperegsystems'
        auto_created = True


class TypeTasksRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='setid')
    typetaskid               = models.ForeignKey('TypeTasks', on_delete=models.CASCADE, db_column='typetaskid')

    class Meta:
        ordering = ('typetaskid',)
        db_table = 'settypetasks'
        auto_created = True


class TypeMiscRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='setid')
    typemiscid                = models.ForeignKey('TypeMisc', on_delete=models.CASCADE, db_column='typemiscid')

    class Meta:
        ordering = ('typemiscid',)
        db_table = 'settypemisc'
        auto_created = True


class ModulesRelationship(models.Model):
    id                       = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='setid')
    moduleid                 = models.ForeignKey('Modules', on_delete=models.CASCADE, db_column='moduleid')

    class Meta:
        ordering = ('moduleid',)
        db_table = 'setmodules'
        auto_created = True


class RegSystemsRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                   = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='setid')
    regsysid                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, db_column='regsysid')

    class Meta:
        ordering = ('regsysid',)
        db_table = 'setregsystems'
        auto_created = True


class drop_deviceRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='setid')
    deviceid             = models.ForeignKey('drop_device', on_delete=models.CASCADE, db_column='deviceid')

    class Meta:
        ordering = ('deviceid',)
        db_table = 'setdevices'
        auto_created = True


class DriversRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='setid')
    driverid                 = models.ForeignKey('Drivers', on_delete=models.CASCADE, db_column='driverid')

    class Meta:
        db_table = 'setdrivers'
        auto_created = True


from django.utils.crypto import get_random_string


def serial():
    return get_random_string(4).upper() + '-' + get_random_string(4).upper() + '-' + get_random_string(4).upper() + '-' + get_random_string(4).upper()


class Distribution(models.Model):
    med = (
        ('нет', 'нет'),
        ('MO', 'MO'),
        ('CD-R', 'CD-R')
    )
    disk = (
        ('Release (S:\)', 'Release (S:\)'),
        ('Repository (R:\)', 'Repository (R:\)')
    )
    spec = (
        ('нет', 'нет'),
        ('ФА', 'ФА'),
        ('Бюллетень', 'Бюллетень')
    )
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setid                   = models.ForeignKey('Sets', on_delete=models.CASCADE, blank=False, db_column='setid')
    organisationid          = models.ForeignKey('Organisations', on_delete=models.CASCADE, blank=False, db_column='organisationid')
    complectno              = models.CharField(max_length=50, blank=True)
    name                    = models.CharField(max_length=50, blank=False)
    date                    = models.DateField(null=False, blank=False, default=datetime.now)
    contract                = models.CharField(max_length=50, blank=True)
    login                   = models.CharField(max_length=50, blank=False)
    serial                  = models.CharField(max_length=50, blank=False, default=serial, unique=True)
    language                = models.CharField(max_length=50, blank=False)
    media                   = models.CharField(max_length=50, blank=True, choices=med)
    os                      = models.CharField(max_length=50, blank=True)
    specialcase             = models.CharField(max_length=50, blank=False, default=None, choices=spec)
    notes                   = models.CharField(max_length=255, blank=True)
    langid                  = models.ForeignKey('Lang_types', on_delete=models.CASCADE, blank=False, db_column='langid')
    osid                    = models.ForeignKey('OS_type', on_delete=models.CASCADE, blank=False, db_column='osid')
    releasedisk             = models.CharField(max_length=50, blank=True, choices=disk)
    distribhaspkeys         = models.ManyToManyField('hasp_keys', blank=True, through='HaspRelationship', through_fields=('distribid', 'haspkeyid'))
    distribhardlockkeys     = models.ManyToManyField('hardlock_keys', blank=True, through='HardLockRelationship', through_fields=('distribid', 'hlkeyid'))
    distribupdate           = models.ManyToManyField('self', blank=True, through='UpdateDistr', through_fields=('distribid', 'distribid'), symmetrical=False)

    def __str__(self):
        return '%s --- %s' % (self.date.strftime('%d.%m.%Y'), self.name)

    class Meta:
        db_table = 'distributions'


class HaspRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    distribid               = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=False, db_column='distribid')
    haspkeyid               = models.ForeignKey('hasp_keys', on_delete=models.CASCADE, blank=False, db_column='haspkeyid')
    date                    = models.DateField(null=False, blank=False, default=datetime.now)

    class Meta:
        db_table = 'distribhaspkeys'
        auto_created = True

    def __str__(self):
        return '%s %s' % (self.date.strftime('%d.%m.%Y'), self.haspkeyid)


class HardLockRelationship(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    distribid               = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=False, db_column='distribid')
    hlkeyid                 = models.ForeignKey('hardlock_keys', on_delete=models.CASCADE, blank=False, db_column='hlkeyid')
    date                    = models.DateField(null=False, blank=False, default=datetime.now)

    class Meta:
        db_table = 'distribhlkeys'
        auto_created = True


class UpdateDistr(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    distribid               = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=False, db_column='distribid')
    newdistribid            = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=True, db_column='newdistribid', related_name='newdistribid_test')
    date                    = models.DateField(null=False, blank=False, default=datetime.now)
    source                  = models.CharField(max_length=80, null=True, blank=True)
    cause                   = models.CharField(max_length=80, null=True, blank=True)
    notes                   = models.CharField(max_length=5192, null=True, blank=True)

    class Meta:
        db_table = 'distribupdates'
        ordering = ('date',)