from django.db import models



class drop_device(models.Model):
    SysName                 = models.CharField(max_length=50)
    UserName                = models.CharField(max_length=50, blank=True)
    ISPath                  = models.CharField(max_length=250, blank=True)
    Description             = models.TextField(max_length=8000, blank=True)

    def __str__(self):
        return 'Системное имя - {0}, Пользовательское имя - {1}, Путь InstallShield - {2}, Описание - {3}'.format(self.SysName, self.UserName, self.ISPath, self.Description)


class hasp_keys(models.Model):
    ChipNo                  = models.CharField(max_length=50)
    Free                    = models.BooleanField(default=False)
    Port                    = models.CharField(max_length=50, blank=True)
    Type                    = models.CharField(max_length=50, blank=True)
    TimeLimit               = models.DateTimeField(null=True, blank=True)
    Licenses                = models.CharField(max_length=250, blank=True)
    Notes                   = models.CharField(max_length=250, blank=True)
