from django.db import models


class drop_device(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=250, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return 'Системное имя - {0}, Пользовательское имя - {1}, Путь InstallShield - {2}, Описание - {3}'.format(self.SysName, self.UserName, self.ISPath, self.Description)


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

    ChipNo                  = models.CharField(max_length=50, blank=False)
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


class plane_types(models.Model):

    SysName                 = models.CharField(max_length=50, blank=False)
    UserName                = models.CharField(max_length=50, blank=False)
    ISPath                  = models.CharField(max_length=250, blank=False)
    Description             = models.TextField(max_length=8000, blank=True)


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


class FASModules(models.Model):

    ExecutableID            = models.ForeignKey(executables, on_delete=models.CASCADE, blank=False, default=id(1))
    FASNo                   = models.IntegerField(blank=False)


class ExecutablePaths(models.Model):

    ExecutableID            = models.ForeignKey(executables, on_delete=models.CASCADE, blank=False, default=id(1))
    ISPath                  = models.CharField(max_length=250, blank=False)
    Source                  = models.CharField(max_length=800, blank=False)
    Dest                    = models.CharField(max_length=800, blank=False)