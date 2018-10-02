from django import forms
from .models import drop_device


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

