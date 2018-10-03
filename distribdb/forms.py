from django import forms
from .models import drop_device, hasp_keys


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

