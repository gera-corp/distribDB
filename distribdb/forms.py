from django import forms
from .models import drop_device, hasp_keys, hardlock_keys, plane_types, Lang_types, OS_type


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
            'Free': 'Свободен?',
            'Port': 'Порт:',
            'Type': 'Тип:',
            'TimeLimit': 'Ограничение по времени:',
            'Licenses': 'Количество лицензий:',
            'Notes': 'Примечания:'
        }
        widgets = {
            'ChipNo': forms.TextInput(attrs={'class': 'form-control'}),
            'Free': forms.CheckboxInput(attrs={'class': 'form-control'}),
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
            'Free': 'Свободен?',
            'Notes': 'Примечания:'
        }
        widgets = {
            'Mark': forms.TextInput(attrs={'class': 'form-control'}),
            'ChipNo': forms.TextInput(attrs={'class': 'form-control'}),
            'Subcode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'ModAddr': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'Port': forms.Select(attrs={'class': 'form-control'}),
            'Free': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Notes': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostPlaneTypeForm(forms.ModelForm):

    class Meta:
        model = plane_types
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
            'ISDefine': forms.TextInput(attrs={'class': 'form-control'}),
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
            'OSCode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
        }