from django import forms
from .models import drop_device


class PostForm(forms.ModelForm):

    class Meta:
        model = drop_device
        fields = ['SysName', 'UserName', 'ISPath', 'Description']
        widgets = {
            'SysName': forms.TextInput(attrs={'class': 'form-control', 'title': 'Пользовательское имя (Attrib)'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control'}),
            'ISPath': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }

