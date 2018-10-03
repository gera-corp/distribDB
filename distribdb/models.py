from django.db import models


class drop_device(models.Model):

    SysName                 = models.CharField(max_length=50)
    UserName                = models.CharField(max_length=50, blank=True)
    ISPath                  = models.CharField(max_length=250, blank=True)
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
