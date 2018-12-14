from django import forms
from .models import *
from django.forms.models import ModelChoiceIterator, ModelMultipleChoiceField
from itertools import groupby


class PostHardlockForm(forms.ModelForm):
    class Meta:
        model = hardlock_keys
        fields = ['mark', 'chipno', 'subcode', 'modaddr', 'port', 'free', 'notes']
        labels = {
            'mark': 'Маркировка:',
            'chipno': 'Номер чипа',
            'subcode': 'Субкод:',
            'modaddr': 'Адрес модуля:',
            'port': 'Порт:',
            'free': 'Свободен:',
            'notes': 'Примечания:'
        }
        widgets = {
            'mark': forms.TextInput(attrs={'class': 'form-control'}),
            'chipno': forms.TextInput(attrs={'class': 'form-control'}),
            'subcode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'modaddr': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'port': forms.Select(attrs={'class': 'form-control'}),
            'free': forms.CheckboxInput(),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostHaspForm(forms.ModelForm):
    class Meta:
        model = hasp_keys
        fields = ['chipno', 'free', 'port', 'type', 'timelimit', 'licenses', 'notes']
        labels = {
            'chipno': 'Номер чипа:',
            'free': 'Свободен:',
            'port': 'Порт:',
            'type': 'Тип:',
            'timelimit': 'Ограничение по времени:',
            'licenses': 'Количество лицензий:',
            'notes': 'Примечания:'
        }
        widgets = {
            'chipno': forms.TextInput(attrs={'class': 'form-control'}),
            'free': forms.CheckboxInput(),
            'port': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'timelimit': forms.DateInput(format="%d.%m.%Y",
                                         attrs={'class': 'form-control', 'placeholder': "дд-мм-гггг"}),
            'licenses': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostPlaneTypeForm(forms.ModelForm):
    class Meta:
        model = Plane_types
        fields = ['sysname', 'username', 'ispath', 'description']
        labels = {
            'sysname': 'Системное имя:',
            'username': 'Пользовательское имя:',
            'ispath': 'Путь InstallShield:',
            'description': 'Описание'
        }
        widgets = {
            'sysname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostLangForm(forms.ModelForm):
    class Meta:
        model = Lang_types
        fields = ['lang', 'lcode', 'isdefine']
        labels = {
            'lang': 'Язык',
            'lcode': 'Код',
            'isdefine': 'Языковая константа'
        }
        widgets = {
            'lang': forms.TextInput(attrs={'class': 'form-control'}),
            'lcode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'isdefine': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostOsForm(forms.ModelForm):
    class Meta:
        model = OS_type
        fields = ['os', 'oscode']
        labels = {
            'os': 'Операционная система',
            'oscode': 'Код'
        }
        widgets = {
            'os': forms.TextInput(attrs={'class': 'form-control'}),
            'oscode': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'})
        }


class PostExecutablesForm(forms.ModelForm):
    class Meta:
        model = executables
        fields = ['filename']
        labels = {
            'filename': 'Имя файла'
        }
        widgets = {
            'filename': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostFASModulesForm(forms.ModelForm):
    class Meta:
        model = FASModules
        fields = ['executableid', 'fasno']
        labels = {
            'executableid': 'Имя файла',
            'fasno': 'FAS-номер'
        }
        widgets = {
            'executableid': forms.Select(attrs={'class': 'form-control'}),
            'fasno': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'})
        }


class PostExecutablePathsForm(forms.ModelForm):
    class Meta:
        model = ExecutablePaths
        fields = ['executableid', 'ispath', 'source', 'dest']
        labels = {
            'executableid': 'Имя файла',
            'ispath': 'Путь InstallShield',
            'source': 'Источник файлов для шифрования',
            'dest': 'Путь для шифрования файлов'

        }
        widgets = {
            'executableid': forms.Select(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'dest': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostRegSystemsForm(forms.ModelForm):
    class Meta:
        model = RegSystems
        fields = ['sysname', 'username', 'ispath', 'hide', 'description']
        labels = {
            'sysname': 'Системное имя',
            'username': 'Пользовательское имя',
            'ispath': 'Путь InstallShield',
            'hide': 'Спрятать',
            'description': 'Описание'

        }
        widgets = {
            'sysname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'hide': forms.CheckboxInput(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostTypeRegsysForm(forms.ModelForm):
    class Meta:
        model = TypeRegsys
        fields = ['typeid', 'regsysid', 'ispath', 'usernameregsys', 'sysnameregsys', 'description']
        labels = {
            'typeid': 'Тип ЛА',
            'regsysid': 'Система регистрации',
            'ispath': 'Путь InstallShield',
            'usernameregsys': 'Пользовательское имя ПБ',
            'sysnameregsys': 'Системное имя ПБ',
            'description': 'Описание'

        }
        widgets = {
            'typeid': forms.Select(attrs={'class': 'form-control'}),
            'regsysid': forms.Select(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'usernameregsys': forms.TextInput(attrs={'class': 'form-control'}),
            'sysnameregsys': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostTasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['sysname', 'username']
        labels = {
            'sysname': 'Системное имя',
            'username': 'Пользовательское имя'
        }
        widgets = {
            'sysname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostTypeTasksForm(forms.ModelForm):
    class Meta:
        model = TypeTasks
        fields = ['typeid', 'taskid', 'ispath', 'description']
        labels = {
            'typeid': 'Тип ЛА',
            'taskid': 'База экспресса',
            'ispath': 'Путь InstallShield',
            'description': 'Описание'
        }
        widgets = {
            'typeid': forms.Select(attrs={'class': 'form-control'}),
            'taskid': forms.Select(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostMiscForm(forms.ModelForm):
    class Meta:
        model = Misc
        fields = ['name', 'sysname', 'username', 'description']
        labels = {
            'name': 'Название',
            'sysname': 'Системное имя',
            'username': 'Пользовательское имя',
            'description': 'Описание'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sysname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostTypeMiscForm(forms.ModelForm):
    class Meta:
        model = TypeMisc
        fields = ['typeid', 'miscid', 'ispath', 'description']
        labels = {
            'typeid': 'Тип ЛА',
            'miscid': 'Элемент',
            'ispath': 'Путь InstallShield',
            'description': 'Описание'
        }
        widgets = {
            'typeid': forms.Select(attrs={'class': 'form-control'}),
            'miscid': forms.Select(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostOrganisationsForm(forms.ModelForm):
    class Meta:
        model = Organisations
        fields = ['name', 'city', 'notes']
        labels = {
            'name': 'Название',
            'city': 'Город',
            'notes': 'Примечания'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostDropDeviceForm(forms.ModelForm):
    class Meta:
        model = drop_device
        fields = ['sysname', 'username', 'ispath', 'description']
        labels = {
            'sysname': 'Системное имя:',
            'username': 'Пользовательское имя:',
            'ispath': 'Путь InstallShield:',
            'description': 'Описание'
        }
        widgets = {
            'sysname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostRegSysDevicesForm(forms.ModelForm):
    class Meta:
        model = RegSysDevices
        fields = ['regsysid', 'deviceid']
        labels = {
            'regsysid': 'Система регистрации',
            'deviceid': 'Устройство сброса'
        }
        widgets = {
            'regsysid': forms.Select(attrs={'class': 'form-control'}),
            'deviceid': forms.Select(attrs={'class': 'form-control'})
        }


class PostModulesForm(forms.ModelForm):
    class Meta:
        model = Modules
        fields = ['name', 'ispath', 'description']
        labels = {
            'name': 'Название',
            'ispath': 'Путь InstallShield',
            'description': 'Описание'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class PostDriversForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = ['name', 'xno', 'ispath', 'description']
        labels = {
            'name': 'Название',
            'xno': 'Группа эксклюзивности(*)',
            'ispath': 'Путь InstallShield',
            'description': 'Описание',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'xno': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'ispath': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})

        }


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
        fields = ['date', 'typeregsystems', 'typetasks', 'typemisc', 'modules', 'regsystems', 'devices', 'drivers']
        labels = {
            'typeregsystems': 'Первичные базы',
            'typetasks': 'Расчётные базы',
            'typemisc': 'Дополнительные элементы',
            'modules': 'Дополнительные модули ПО',
            'regsystems': 'Системы решистрации',
            'devices': 'Устройства сброса',
            'drivers': 'Драйверы устройств'
        }

        widgets = {
            'date': forms.DateInput(format="%d.%m.%Y", attrs={'class': 'form-control', 'placeholder': "дд-мм-гггг"}),
            'modules': forms.CheckboxSelectMultiple(),
            'regsystems': forms.CheckboxSelectMultiple(),
            'devices': forms.CheckboxSelectMultiple(),
            'drivers': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(WidgetForm, self).__init__(*args, **kwargs)
        self.fields['typeregsystems'] = GroupedModelMultipleChoiceField(group_by_field='typeid',
                                                                  queryset=TypeRegsys.objects.select_related('regsysid'),
                                                                  widget=GroupedCheckboxSelectMultiple(),
                                                                  required=False)
        self.fields['typetasks'] = GroupedModelMultipleChoiceField(group_by_field='typeid',
                                                                     queryset=TypeTasks.objects.select_related('taskid'),
                                                                     widget=GroupedCheckboxSelectMultiple(),
                                                                     required=False)
        self.fields['typemisc'] = GroupedModelMultipleChoiceField(group_by_field='typeid',
                                                                    queryset=TypeMisc.objects.select_related('miscid'),
                                                                    widget=GroupedCheckboxSelectMultiple(),
                                                                    required=False)


class Distrib(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = [
            'name',
            'setid',
            'date',
            'organisationid',
            'complectno',
            'contract',
            'login',
            'serial',
            #'language',
            #'os',
            'langid',
            'media',
            'osid',
            'specialcase',
            'releasedisk',
            'notes',
            'distribhaspkeys',
            'distribhardlockkeys'
        ]
        labels = {
            'setid': 'Набор',
            'organisationid': 'Заказчик',
            'complectno': '№ комплекта',
            'name': 'Название',
            'date': 'Дата создания дистрибутива',
            'contract': 'Контракт',
            'login': 'Логин',
            'serial': 'Серийный номер',
            # 'language': 'Язык',
            'media': 'Носитель',
            # 'os': 'Операционная система',
            'langid': 'Язык',
            'osid': 'Операционная система',
            'specialcase': 'Особые условия',
            'releasedisk': 'Диск сборки',
            'notes': 'Примечания',
            'distribhaspkeys': 'Ключи дистрибутива HASP',
            'distribhardlockkeys': 'Ключи дистрибутива Hardlock'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'setid': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(format="%d.%m.%Y", attrs={'class': 'form-control', 'placeholder': "дд-мм-гггг"}),
            'organisationid': forms.Select(attrs={'class': 'form-control'}),
            'complectno': forms.TextInput(attrs={'class': 'form-control'}),
            'contract': forms.TextInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            #'language': forms.TextInput(attrs={'class': 'form-control'}),
            'media': forms.Select(attrs={'class': 'form-control'}),
            #'os': forms.TextInput(attrs={'class': 'form-control'}),
            'langid': forms.Select(attrs={'class': 'form-control'}),
            'osid': forms.Select(attrs={'class': 'form-control'}),
            'specialcase': forms.Select(attrs={'class': 'form-control'}),
            'releasedisk': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'distribhaspkeys': forms.CheckboxSelectMultiple(),
            'distribhardlockkeys': forms.CheckboxSelectMultiple()

        }


class DistribUpdate(forms.ModelForm):
    class Meta:
        model = UpdateDistr
        fields = [
            'distribid',
            'newdistribid',
            'date',
            'source',
            'cause',
            'notes'
        ]
        labels = {
            'distribid': 'Обновляемый дистрибутив:',
            'newdistribid': 'Новое название дистрибутива:',
            'date': 'Дата обновления:',
            'source': 'Кто запросил:',
            'cause': 'Причина обновления:',
            'notes': 'Примечания:'
        }
        widgets = {
            'distribid': forms.Select(attrs={'class': 'form-control'}),
            'newdistribid': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'cause': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'})
        }