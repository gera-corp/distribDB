from django.db import models
from datetime import datetime
import uuid


class hardlock_keys(models.Model):
    port_name = (
        ('USB', 'USB'),
        ('LPT', 'LPT')
    )
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
        db_table = 'HL_Keys'

    def __str__(self):
        return self.ChipNo


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
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ChipNo                  = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Номером чипа')
    Free                    = models.BooleanField(default=False)
    Port                    = models.CharField(max_length=50, blank=False, default=None, choices=port_name)
    Type                    = models.CharField(max_length=50, blank=False, default=None, choices=type_key)
    TimeLimit               = models.DateField(null=True, blank=True)
    Licenses                = models.CharField(max_length=255, blank=True, null=True)
    Notes                   = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.ChipNo

    class Meta:
        verbose_name = 'Ключ аппаратной защиты (HASP)'
        ordering = ('ChipNo',)
        db_table = 'HASP_Keys'


class Plane_types(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=250, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.UserName

    class Meta:
        ordering = ('UserName',)
        verbose_name = 'Типы ЛА'
        db_table = 'PlaneTypes'


class Lang_types(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Lang                    = models.CharField(max_length=50, blank=False)
    LCode                   = models.IntegerField()
    ISDefine                = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.Lang

    class Meta:
        db_table = 'Lang'


class OS_type(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    OS                      = models.CharField(max_length=50, blank=False)
    OSCode                  = models.IntegerField(blank=False)

    def __str__(self):
        return self.OS

    class Meta:
        db_table = 'OS'


class executables(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FileName                = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Именем файла')

    def __str__(self):
        return self.FileName

    class Meta:
        verbose_name = 'Исполняемый модуль'
        ordering = ('FileName',)
        db_table = 'Executables'


class FASModules(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ExecutableID            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, db_column='ExecutableID')
    FASNo                   = models.IntegerField(blank=False, unique=True, verbose_name='FAS номером')

    class Meta:
        verbose_name = 'FAS модуль'
        ordering = ('ExecutableID',)
        db_table = 'FASModules'


class ExecutablePaths(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ExecutableID            = models.ForeignKey('executables', on_delete=models.CASCADE, blank=False, db_column='ExecutableID')
    ISPath                  = models.CharField(max_length=250, blank=False)
    Source                  = models.CharField(max_length=800, blank=True)
    Dest                    = models.CharField(max_length=800, blank=True)

    class Meta:
        ordering = ('ExecutableID',)
        db_table = 'ExecutablePaths'


class RegSystems(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=50, blank=False)
    Hide                    = models.BooleanField(default=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return '%s %s' % (self.UserName, self.Hide)

    class Meta:
        ordering = ('UserName',)
        db_table = 'RegSystems'


class TypeRegsys(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА', db_column='TypeID')
    RegsysID                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, verbose_name='Система регистрации', db_column='RegsysID')
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
        db_table = 'TypeRegsys'


class Tasks(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SysName                 = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Системным именем')
    UserName                = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.SysName

    class Meta:
        verbose_name = 'База экспрессов'
        ordering = ('SysName',)
        db_table = 'Tasks'


class TypeTasks(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА', db_column='TypeID')
    TaskID                  = models.ForeignKey('Tasks', on_delete=models.CASCADE, blank=False, verbose_name='База экспресса', db_column='TaskID')
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.TaskID.SysName

    class Meta:
        ordering = ('TypeID',)
        verbose_name = 'Экспресс для типов ЛА'
        unique_together = ('TypeID', 'TaskID')
        db_table = 'TypeTasks'


class Misc(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name                    = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Названием')
    SysName                 = models.CharField(max_length=50, blank=True)
    UserName                = models.CharField(max_length=50, blank=True)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Допольнительный элемент ЛА'
        ordering = ('Name',)
        db_table = 'Misc'


class TypeMisc(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TypeID                  = models.ForeignKey('Plane_types', on_delete=models.CASCADE, blank=False, verbose_name='Тип ЛА', db_column='TypeID')
    MiscID                  = models.ForeignKey('Misc', on_delete=models.CASCADE, blank=False, verbose_name='Элемент', db_column='MiscID')
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.MiscID.Name

    class Meta:
        verbose_name = 'Дополнительный элемент ЛА'
        unique_together = ('TypeID', 'MiscID')
        ordering = ('TypeID',)
        db_table = 'TypeMisc'


class Organisations(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name                    = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Названием')
    City                    = models.CharField(max_length=50, blank=True)
    Notes                   = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Организация'
        ordering = ('Name',)
        db_table = 'Organisations'


class drop_device(models.Model):
    ID                       = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SysName                  = models.CharField(max_length=50, blank=False)
    UserName                 = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Пользовательским именем')
    ISPath                   = models.CharField(max_length=250, blank=False)
    Description              = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.UserName

    class Meta:
        verbose_name = 'Устройство сброса'
        ordering = ('UserName',)
        db_table = 'Devices'


class RegSysDevices(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RegsysID                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, blank=False, db_column='RegsysID')
    DeviceID                = models.ForeignKey('drop_device', on_delete=models.CASCADE, blank=False, db_column='DeviceID')

    def __str__(self):
        return '%s %s' % (self.RegsysID.UserName, self.DeviceID.UserName)

    class Meta:
        ordering = ('RegsysID',)
        db_table = 'RegSysDevices'


class Modules(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name                    = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Названием')
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Дополнительный модуль ПО'
        ordering = ('Name',)
        db_table = 'Modules'


class Drivers(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name                    = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Названием')
    Xno                     = models.IntegerField(blank=False)
    ISPath                  = models.CharField(max_length=255, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Драйвер'
        ordering = ('Name',)
        db_table = 'Drivers'


def ids():
    try:
        no = Sets.objects.first().UserFriendlyID
        return no + 1
    except:
        return 1


class Sets(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserFriendlyID          = models.BigIntegerField(default=ids, unique=True, editable=False)
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)
    typeregsystems          = models.ManyToManyField('TypeRegsys', through='TypeRegSysRelationship', through_fields=('SetID', 'TypeRegsysID'))
    typetasks               = models.ManyToManyField('TypeTasks', through='TypeTasksRelationship', through_fields=('SetID', 'TypeTaskID'))
    typemisc                = models.ManyToManyField('TypeMisc', through='TypeMiscRelationship', through_fields=('SetID', 'TypeMiscID'))
    modules                 = models.ManyToManyField('Modules', through='ModulesRelationship', through_fields=('SetID', 'ModuleID'), blank=True)
    regsystems              = models.ManyToManyField('RegSystems', through='RegSystemsRelationship', through_fields=('SetID', 'RegsysID'), blank=True)
    devices                 = models.ManyToManyField('drop_device', through='drop_deviceRelationship', through_fields=('SetID', 'DeviceID'), blank=True)
    drivers                 = models.ManyToManyField('Drivers', through='DriversRelationship', through_fields=('SetID', 'DriverID'), blank=True)

    def __str__(self):
        return '%s --- %s' % (self.Date.strftime('%d.%m.%Y'), self.UserFriendlyID)

    class Meta:
        ordering = ('-UserFriendlyID',)
        db_table = 'Sets'


class TypeRegSysRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='SetID')
    TypeRegsysID              = models.ForeignKey('TypeRegsys', on_delete=models.CASCADE, db_column='TypeRegsysID')

    class Meta:
        ordering = ('TypeRegsysID',)
        db_table = 'SetTypeRegsystems'
        auto_created = True


class TypeTasksRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='SetID')
    TypeTaskID               = models.ForeignKey('TypeTasks', on_delete=models.CASCADE, db_column='TypeTaskID')

    class Meta:
        ordering = ('TypeTaskID',)
        db_table = 'SetTypeTasks'
        auto_created = True


class TypeMiscRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='SetID')
    TypeMiscID                = models.ForeignKey('TypeMisc', on_delete=models.CASCADE, db_column='TypeMiscID')

    class Meta:
        ordering = ('TypeMiscID',)
        db_table = 'SetTypeMisc'
        auto_created = True


class ModulesRelationship(models.Model):
    ID                       = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='SetID')
    ModuleID                 = models.ForeignKey('Modules', on_delete=models.CASCADE, db_column='ModuleID')

    class Meta:
        ordering = ('ModuleID',)
        db_table = 'SetModules'
        auto_created = True


class RegSystemsRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                   = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='SetID')
    RegsysID                = models.ForeignKey('RegSystems', on_delete=models.CASCADE, db_column='RegsysID')

    class Meta:
        ordering = ('RegsysID',)
        db_table = 'SetRegsystems'
        auto_created = True


class drop_deviceRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='SetID')
    DeviceID             = models.ForeignKey('drop_device', on_delete=models.CASCADE, db_column='DeviceID')

    class Meta:
        ordering = ('DeviceID',)
        db_table = 'SetDevices'
        auto_created = True


class DriversRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                    = models.ForeignKey('Sets', on_delete=models.CASCADE, db_column='SetID')
    DriverID                 = models.ForeignKey('Drivers', on_delete=models.CASCADE, db_column='DriverID')

    class Meta:
        db_table = 'SetDrivers'
        auto_created = True


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
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SetID                   = models.ForeignKey('Sets', on_delete=models.CASCADE, blank=False, db_column='SetID')
    OrganisationID          = models.ForeignKey('Organisations', on_delete=models.CASCADE, blank=False, db_column='OrganisationID')
    ComplectNo              = models.CharField(max_length=50, blank=True)
    Name                    = models.CharField(max_length=50, blank=False)
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)
    Contract                = models.CharField(max_length=50, blank=True)
    Login                   = models.CharField(max_length=50, blank=False)
    Serial                  = models.CharField(max_length=50, blank=False)
    Language                = models.CharField(max_length=50, blank=False)
    Media                   = models.CharField(max_length=50, blank=True, choices=med)
    OS                      = models.CharField(max_length=50, blank=True)
    SpecialCase             = models.CharField(max_length=50, blank=False, choices=spec)
    Notes                   = models.CharField(max_length=255, blank=True)
    LangID                  = models.ForeignKey('Lang_types', on_delete=models.CASCADE, blank=False, db_column='LangID')
    osID                    = models.ForeignKey('OS_type', on_delete=models.CASCADE, blank=False, db_column='osID')
    ReleaseDisk             = models.CharField(max_length=50, blank=True, choices=disk)
    distribhaspkeys         = models.ManyToManyField('hasp_keys', blank=True, through='HaspRelationship', through_fields=('DistribID', 'HASPKeyID'))
    distribhardlockkeys     = models.ManyToManyField('hardlock_keys', blank=True, through='HardLockRelationship', through_fields=('DistribID', 'HLKeyID'))
    distribupdate           = models.ManyToManyField('self', blank=True, through='UpdateDistr', through_fields=('DistribID', 'DistribID'), symmetrical=False)

    def __str__(self):
        return '%s --- %s' % (self.Date.strftime('%d.%m.%Y'), self.Name)

    class Meta:
        db_table = 'Distributions'


class HaspRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DistribID               = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=False, db_column='DistribID')
    HASPKeyID               = models.ForeignKey('hasp_keys', on_delete=models.CASCADE, blank=False, db_column='HASPKeyID')
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)

    class Meta:
        db_table = 'DistribHASPKeys'
        auto_created = True

    def __str__(self):
        return '%s %s' % (self.Date.strftime('%d.%m.%Y'), self.HASPKeyID)


class HardLockRelationship(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DistribID               = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=False, db_column='DistribID')
    HLKeyID                 = models.ForeignKey('hardlock_keys', on_delete=models.CASCADE, blank=False, db_column='HLKeyID')
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)

    class Meta:
        db_table = 'DistribHLKeys'
        auto_created = True


class UpdateDistr(models.Model):
    ID                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DistribID               = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=False, db_column='DistribID')
    NewDistribID            = models.ForeignKey('Distribution', on_delete=models.CASCADE, blank=True, db_column='NewDistribID', related_name='newdistribid_test')
    Date                    = models.DateField(null=False, blank=False, default=datetime.now)
    Source                  = models.CharField(max_length=80, null=True, blank=True)
    Cause                   = models.CharField(max_length=80, null=True, blank=True)
    Notes                   = models.CharField(max_length=5192, null=True, blank=True)

    class Meta:
        db_table = 'DistribUpdates'
        ordering = ('Date',)