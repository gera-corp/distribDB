from django.db import models



class drop_device(models.Model):
    SysName                 = models.CharField(max_length=250)
    UserName                = models.CharField(max_length=250)
    ISPath                  = models.CharField(max_length=250)
    Description             = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return 'Системное имя - {0}, Пользовательское имя - {1}, Путь InstallShield - {2}, Описание - {3}'.format(self.SysName, self.UserName, self.ISPath, self.Description)



