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
#     RegsysID = forms.ModelMultipleChoiceField(queryset=TypeRegsys.objects.all().order_by('TypeID'), widget=forms.CheckboxSelectMultiple())
#
#     class Meta:
#         model = Sets
#         fields = [
#             'Date',
#             'UserFriendlyID',
#             'RegsysID',
#             'TypeTasksID',
#             'TypeMiscID',
#             'RegSysDevicesID'
#         ]
#
#         labels = {
#             'UserFriendlyID': 'ID',
#             'Date': 'Дата',
#             'RegsysID': 'Тип ЛА',
#             'TypeTasksID': '',
#             'TypeMiscID': '',
#             'RegSysDevicesID': ''
#         }
#
#         widgets = {
#             'UserFriendlyID': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Date': forms.DateInput(format="%d.%m.%Y", attrs={'class': 'form-control', 'placeholder': "дд-мм-гггг"}),
#             # 'RegsysID': forms.CheckboxSelectMultiple(),
#             'TypeTasksID': forms.CheckboxSelectMultiple(),
#             'TypeMiscID': forms.CheckboxSelectMultiple(),
#             'RegSysDevicesID': forms.CheckboxSelectMultiple(),
#           }


from django.forms.models import ModelChoiceIterator, ModelMultipleChoiceField
from itertools import groupby


class GroupedModelMultipleChoiceField(ModelMultipleChoiceField):

    def __init__(self, group_by_field, group_label=None, *args, **kwargs):
        """
        ``group_by_field`` is the name of a field on the model
        ``group_label`` is a function to return a label for each choice group

        """
        super(GroupedModelMultipleChoiceField, self).__init__(*args, **kwargs)
        self.group_by_field = group_by_field
        if group_label is None:
            self.group_label = lambda group: group
        else:
            self.group_label = group_label

    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return GroupedModelChoiceIterator(self)
    choices = property(_get_choices, ModelMultipleChoiceField._set_choices)


class GroupedModelChoiceIterator(ModelChoiceIterator):

    def __iter__(self):
        """Now yields grouped choices."""
        if self.field.empty_label is not None:
            yield ("", self.field.empty_label)
        for group, choices in groupby(
                self.queryset.all(),
                lambda row: getattr(row, self.field.group_by_field)):
            if group is None:
                for ch in choices:
                    yield self.choice(ch)
            else:
                yield (
                    self.field.group_label(group),
                    [self.choice(ch) for ch in choices])


class GroupedCheckboxSelectMultiple(forms.CheckboxSelectMultiple):

    def optgroups(self, name, value, attrs=None):
        """
        The group name is passed as an argument to the ``create_option`` method (below).

        """
        groups = []
        has_selected = False

        for index, (option_value, option_label) in enumerate(self.choices):
            if option_value is None:
                option_value = ''

            subgroup = []
            if isinstance(option_label, (list, tuple)):
                group_name = option_value
                subindex = 0
                choices = option_label
            else:
                group_name = None
                subindex = None
                choices = [(option_value, option_label)]
            groups.append((group_name, subgroup, index))

            for subvalue, sublabel in choices:
                selected = (
                    str(subvalue) in value and
                    (not has_selected or self.allow_multiple_selected)
                )
                has_selected |= selected
                subgroup.append(self.create_option(
                    name, subvalue, sublabel, selected, index,
                    subindex=subindex, attrs=attrs, group=group_name,
                ))
                if subindex is not None:
                    subindex += 1
        return groups

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None, group=None):
        """
        Added a ``group`` argument which is included in the returned dictionary.

        """
        index = str(index) if subindex is None else "%s_%s" % (index, subindex)
        if attrs is None:
            attrs = {}
        option_attrs = self.build_attrs(self.attrs, attrs) if self.option_inherits_attrs else {}
        if selected:
            option_attrs.update(self.checked_attribute)
        if 'id' in option_attrs:
            option_attrs['id'] = self.id_for_label(option_attrs['id'], index)
        return {
            'name': name,
            'value': value,
            'label': label,
            'selected': selected,
            'index': index,
            'attrs': option_attrs,
            'type': self.input_type,
            'template_name': self.option_template_name,
            'wrap_label': True,
            'group': group,
        }


class WidgetForm(forms.ModelForm):
    class Meta:
        model = Sets
        fields = ['RegsysID', 'TypeTasksID', 'Date']
        labels = {
            'RegsysID': 'Первичные базы',
            'TypeTasksID': 'Расчётные базы',
        }

        widgets = {
            'Date': forms.DateInput(format="%d.%m.%Y", attrs={'class': 'form-control', 'placeholder': "дд-мм-гггг"}),
        }

    def __init__(self, *args, **kwargs):
        super(WidgetForm, self).__init__(*args, **kwargs)
        self.fields['RegsysID'] = GroupedModelMultipleChoiceField(group_by_field='TypeID', queryset=TypeRegsys.objects.all(), widget=GroupedCheckboxSelectMultiple(), required=False)
        self.fields['TypeTasksID'] = GroupedModelMultipleChoiceField(group_by_field='TypeID', queryset=TypeTasks.objects.all(), widget=GroupedCheckboxSelectMultiple(), required=False)
