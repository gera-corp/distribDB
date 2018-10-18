from django import forms
from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = drop_device
        fields = ['SysName', 'UserName', 'ISPath', 'Description']
        labels = {
            'SysName': 'Пользовательское имя:',
            'UserName': 'Системное имя:',
            'ISPath': 'Путь InstallShield:',
            'Description': 'Описание'
        }
        widgets = {
            'SysName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Attrib"}),
            'UserName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "имя каталога"}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostHaspForm(forms.ModelForm):

    class Meta:
        model = hasp_keys
        fields = ['ChipNo', 'Free', 'Port', 'Type', 'TimeLimit', 'Licenses', 'Notes']
        labels = {
            'ChipNo': 'Номер чипа:',
            'Free': 'Свободен:',
            'Port': 'Порт:',
            'Type': 'Тип:',
            'TimeLimit': 'Ограничение по времени:',
            'Licenses': 'Количество лицензий:',
            'Notes': 'Примечания:'
        }
        widgets = {
            'ChipNo': forms.TextInput(attrs={'class': 'form-control'}),
            'Free': forms.CheckboxInput(),
            'Port': forms.Select(attrs={'class': 'form-control'}),
            'Type': forms.Select(attrs={'class': 'form-control'}),
            'TimeLimit': forms.DateInput(format="%d.%m.%Y", attrs={'class': 'form-control', 'placeholder': "дд-мм-гггг"}),
            'Licenses': forms.TextInput(attrs={'class': 'form-control'}),
            'Notes': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostHardlockForm(forms.ModelForm):

    class Meta:
        model = hardlock_keys
        fields = ['Mark', 'ChipNo', 'Subcode', 'ModAddr', 'Port', 'Free', 'Notes']
        labels = {
            'Mark': 'Маркировка:',
            'ChipNo': 'Номер чипа',
            'Subcode': 'Субкод:',
            'ModAddr': 'Адрес модуля:',
            'Port': 'Порт:',
            'Free': 'Свободен:',
            'Notes': 'Примечания:'
        }
        widgets = {
            'Mark': forms.TextInput(attrs={'class': 'form-control'}),
            'ChipNo': forms.TextInput(attrs={'class': 'form-control'}),
            'Subcode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'ModAddr': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'Port': forms.Select(attrs={'class': 'form-control'}),
            'Free': forms.CheckboxInput(),
            'Notes': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostPlaneTypeForm(forms.ModelForm):

    class Meta:
        model = Plane_types
        fields = ['SysName', 'UserName', 'ISPath', 'Description']
        labels = {
            'SysName': 'Системное имя:',
            'UserName': 'Пользовательское имя:',
            'ISPath': 'Путь InstallShield:',
            'Description': 'Описание'
        }
        widgets = {
            'SysName': forms.TextInput(attrs={'class': 'form-control'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostLangForm(forms.ModelForm):

    class Meta:
        model = Lang_types
        fields = ['Lang', 'LCode', 'ISDefine']
        labels = {
            'Lang': 'Язык',
            'LCode': 'Код',
            'ISDefine': 'Языковая константа'
        }
        widgets = {
            'Lang': forms.TextInput(attrs={'class': 'form-control'}),
            'LCode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'ISDefine': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostOsForm(forms.ModelForm):

    class Meta:
        model = OS_type
        fields = ['OS', 'OSCode']
        labels = {
            'OS': 'Операционная система',
            'OSCode': 'Код'
        }
        widgets = {
            'OS': forms.TextInput(attrs={'class': 'form-control'}),
            'OSCode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'})
        }


class PostExecutablesForm(forms.ModelForm):

    class Meta:
        model = executables
        fields = ['FileName']
        labels = {
            'FileName': 'Имя файла'
        }
        widgets = {
            'FileName': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostFASModulesForm(forms.ModelForm):

    class Meta:
        model = FASModules
        fields = ['ExecutableID', 'FASNo']
        labels = {
            'ExecutableID': 'Имя файла',
            'FASNo': 'FAS-номер'
        }
        widgets = {
            'ExecutableID': forms.Select(attrs={'class': 'form-control'}),
            'FASNo': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'})
        }


class PostExecutablePathsForm(forms.ModelForm):

    class Meta:
        model = ExecutablePaths
        fields = ['ExecutableID', 'ISPath', 'Source', 'Dest']
        labels = {
            'ExecutableID': 'Имя файла',
            'ISPath': 'Путь InstallShield',
            'Source': 'Источник файлов для шифрования',
            'Dest': 'Путь для шифрования файлов'

        }
        widgets = {
            'ExecutableID': forms.Select(attrs={'class': 'form-control'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Source': forms.TextInput(attrs={'class': 'form-control'}),
            'Dest': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostRegSystemsForm(forms.ModelForm):

    class Meta:
        model = RegSystems
        fields = ['SysName', 'UserName', 'ISPath', 'Hide', 'Description']
        labels = {
            'SysName': 'Системное имя',
            'UserName': 'Пользовательское имя',
            'ISPath': 'Путь InstallShield',
            'Hide': 'Спрятать',
            'Description': 'Описание'

        }
        widgets = {
            'SysName': forms.TextInput(attrs={'class': 'form-control'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Hide': forms.CheckboxInput(),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostTypeRegsysForm(forms.ModelForm):

    class Meta:
        model = TypeRegsys
        fields = ['TypeID', 'RegsysID', 'ISPath', 'UserNameRegsys', 'SysNameRegsys', 'Description']
        labels = {
            'TypeID': 'Тип ЛА',
            'RegsysID': 'Система регистрации',
            'ISPath': 'Путь InstallShield',
            'UserNameRegsys': 'Пользовательское имя ПБ',
            'SysNameRegsys': 'Системное имя ПБ',
            'Description': 'Описание'

        }
        widgets = {
            'TypeID': forms.Select(attrs={'class': 'form-control'}),
            'RegsysID': forms.Select(attrs={'class': 'form-control'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'UserNameRegsys': forms.TextInput(attrs={'class': 'form-control'}),
            'SysNameRegsys': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostTasksForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ['SysName', 'UserName']
        labels = {
            'SysName': 'Системное имя',
            'UserName': 'Пользовательское имя'
        }
        widgets = {
            'SysName': forms.TextInput(attrs={'class': 'form-control'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostTypeTasksForm(forms.ModelForm):

    class Meta:
        model = TypeTasks
        fields = ['TypeID', 'TaskID', 'ISPath', 'Description']
        labels = {
            'TypeID': 'Тип ЛА',
            'TaskID': 'База экспресса',
            'ISPath': 'Путь InstallShield',
            'Description': 'Описание'
        }
        widgets = {
            'TypeID': forms.Select(attrs={'class': 'form-control'}),
            'TaskID': forms.Select(attrs={'class': 'form-control'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostMiscForm(forms.ModelForm):

    class Meta:
        model = Misc
        fields = ['Name', 'SysName', 'UserName', 'Description']
        labels = {
            'Name': 'Название',
            'SysName': 'Системное имя',
            'UserName': 'Пользовательское имя',
            'Description': 'Описание'
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'SysName': forms.TextInput(attrs={'class': 'form-control'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostTypeMiscForm(forms.ModelForm):

    class Meta:
        model = TypeMisc
        fields = ['TypeID', 'MiscID', 'ISPath', 'Description']
        labels = {
            'TypeID': 'Тип ЛА',
            'MiscID': 'Элемент',
            'ISPath': 'Путь InstallShield',
            'Description': 'Описание'
        }
        widgets = {
            'TypeID': forms.Select(attrs={'class': 'form-control'}),
            'MiscID': forms.Select(attrs={'class': 'form-control'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostOrganisationsForm(forms.ModelForm):

    class Meta:
        model = Organisations
        fields = ['Name', 'City', 'Notes']
        labels = {
            'Name': 'Название',
            'City': 'Город',
            'Notes': 'Примечания'
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'Notes': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostRegSysDevicesForm(forms.ModelForm):

    class Meta:
        model = RegSysDevices
        fields = ['RegsysID', 'DeviceID']
        labels = {
            'RegsysID': 'Система регистрации',
            'DeviceID': 'Устройство сброса'
        }
        widgets = {
            'RegsysID': forms.Select(attrs={'class': 'form-control'}),
            'DeviceID': forms.Select(attrs={'class': 'form-control'})
        }


class PostModulesForm(forms.ModelForm):

    class Meta:
        model = Modules
        fields = ['Name', 'Description', 'ISPath']
        labels = {
            'Name': 'Название',
            'Description': 'Описание',
            'ISPath': 'Путь InstallShield'
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostDriversForm(forms.ModelForm):

    class Meta:
        model = Drivers
        fields = ['Name', 'Xno', 'ISPath', 'Description']
        labels = {
            'Name': 'Название',
            'Xno': 'Группа эксклюзивности(*)',
            'ISPath': 'Путь InstallShield',
            'Description': 'Описание',

        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Xno': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})

        }


# class PostEditSetForm(forms.ModelForm):
#
#     class Meta:
#         model = Sets
#         fields = ['Date', 'UserFriendlyID', 'RegsysID', 'TypeTasksID', 'TypeMiscID', 'RegSysDevicesID']
#         labels = {
#             'UserFriendlyID': 'ID',
#             'Date': 'Дата',
#             'RegsysID': '',
#             'TypeTasksID': '',
#             'TypeMiscID': '',
#             'RegSysDevicesID': ''
#         }
#         widgets = {
#             'UserFriendlyID': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Date': forms.DateInput(format="%d.%m.%Y", attrs={'class': 'form-control', 'placeholder': "дд-мм-гггг"}),
#             'RegsysID': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 5}),
#             'TypeTasksID': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 5}),
#             'TypeMiscID': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 5}),
#             'RegSysDevicesID': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 5}),
#         }


class PersonForm(forms.ModelForm):
    class Meta:
        model = Sets
        fields = ('Date', 'UserFriendlyID', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = TypeRegsys.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = TypeRegsys.objects.filter(RegsysID_id=country_id).order_by('id')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('TypeID')