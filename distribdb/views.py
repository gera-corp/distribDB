from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import *


def home(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    return render(request, 'index.html')


def tables(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    return render(request, 'tables.html')


def programms(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    return render(request, 'programms.html')


def drop_device_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = drop_device.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(sysname__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/drop_devices.html', context)


def drop_device_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(drop_device, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/drop_devices')
    return render(request, 'tables/drop_devices.html', {'device': obj})


def drop_device_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/drop_device_new_post.html'
    form = PostDropDeviceForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового устройства добавлена!')
            form = PostDropDeviceForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def drop_device_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/drop_device_new_post.html'
    post = get_object_or_404(drop_device, pk=pk)

    if request.method == 'POST':
        form = PostDropDeviceForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostDropDeviceForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def hasp_keys_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = hasp_keys.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
             Q(chipno__icontains=query) |
             Q(notes__icontains=query)
         ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20) #Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/hasp_keys.html', context)


def hasp_keys_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(hasp_keys, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/hasp_keys')
    return render(request, 'tables/hasp_keys.html', {'device': obj})


def hasp_keys_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/hasp_keys_new_post.html'
    form = PostHaspForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового ключа добавлена!')
            form = PostHaspForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def hasp_keys_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/hasp_keys_new_post.html'
    post = get_object_or_404(hasp_keys, pk=pk)

    if request.method == 'POST':
        form = PostHaspForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostHaspForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def hardlock_keys_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = hardlock_keys.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(chipno__icontains=query) |
            Q(notes__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/hardlock_keys.html', context)


def hardlock_keys_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(hardlock_keys, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/hardlock_keys')
    return render(request, 'tables/hardlock_keys.html', {'device': obj})


def hardlock_keys_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/hardlock_keys_new_post.html'
    form = PostHardlockForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового ключа добавлена!')
            form = PostHardlockForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def hardlock_keys_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/hardlock_keys_new_post.html'
    post = get_object_or_404(hardlock_keys, pk=pk)

    if request.method == 'POST':
        form = PostHardlockForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostHardlockForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def plane_types_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Plane_types.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(sysname__icontains=query) |
            Q(username__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/plane_types.html', context)


def plane_types_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Plane_types, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/plane_types')
    return render(request, 'tables/plane_types.html', {'device': obj})


def plane_types_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/plane_types_new_post.html'
    form = PostPlaneTypeForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового типа добавлена!')
            form = PostPlaneTypeForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def plane_types_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/plane_types_new_post.html'
    post = get_object_or_404(Plane_types, pk=pk)

    if request.method == 'POST':
        form = PostPlaneTypeForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostPlaneTypeForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def lang_types_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Lang_types.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(lang__icontains=query) |
            Q(lcode__icontains=query) |
            Q(isdefine__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/lang_types.html', context)


def lang_types_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Lang_types, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/lang_types')
    return render(request, 'tables/lang_types.html', {'device': obj})


def lang_types_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/lang_types_new_post.html'
    form = PostLangForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового языка добавлена!')
            form = PostLangForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def lang_types_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/lang_types_new_post.html'
    post = get_object_or_404(Lang_types, pk=pk)

    if request.method == 'POST':
        form = PostLangForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostLangForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def os_types_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = OS_type.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(os__icontains=query) |
            Q(oscode__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/os_types.html', context)


def os_types_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(OS_type, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/os_types')
    return render(request, 'tables/os_types.html', {'device': obj})


def os_types_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/os_types_new_post.html'
    form = PostOsForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись новой OS добавлена!')
            form = PostOsForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def os_types_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/os_types_new_post.html'
    post = get_object_or_404(OS_type, pk=pk)

    if request.method == 'POST':
        form = PostOsForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostOsForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def executables_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = executables.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(filename__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/executables.html', context)


def executables_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(executables, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/executables')
    return render(request, 'tables/executables.html', {'device': obj})


def executables_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/executables_new_post.html'
    form = PostExecutablesForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового модуля добавлена!')
            form = PostExecutablesForm
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def executables_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/executables_new_post.html'
    post = get_object_or_404(executables, pk=pk)

    if request.method == 'POST':
        form = PostExecutablesForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostExecutablesForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def fas_modules_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = FASModules.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(executableid__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/fas_modules.html', context)


def fas_modules_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(FASModules, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/fas_modules')
    return render(request, 'tables/fas_modules.html', {'device': obj})


def fas_modules_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/fas_modules_new_post.html'
    form = PostFASModulesForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового номера FAS добавлена!')
            form = PostFASModulesForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def fas_modules_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/fas_modules_new_post.html'
    post = get_object_or_404(FASModules, pk=pk)

    if request.method == 'POST':
        form = PostFASModulesForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostFASModulesForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def executable_paths_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = ExecutablePaths.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(ExecutableID__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/executable_paths.html', context)


def executable_paths_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(ExecutablePaths, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/executable_paths')
    return render(request, 'tables/executable_paths.html', {'device': obj})


def executable_paths_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/executable_paths_new_post.html'
    form = PostExecutablePathsForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового пути InstallShield добавлена!')
            form = PostExecutablePathsForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def executable_paths_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/executable_paths_new_post.html'
    post = get_object_or_404(ExecutablePaths, pk=pk)

    if request.method == 'POST':
        form = PostExecutablePathsForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostExecutablePathsForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def regsystems_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = RegSystems.objects.all().order_by('sysname')
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(sysname__icontains=query) |
            Q(username__icontains=query) |
            Q(ispath__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/regsystems.html', context)


def regsystems_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(RegSystems, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/regsystems')
    return render(request, 'tables/regsystems.html', {'device': obj})


def regsystems_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/regsystems_new_post.html'
    form = PostRegSystemsForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись новой системы регистрации добавлена!')
            form = PostRegSystemsForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def regsystems_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/regsystems_new_post.html'
    post = get_object_or_404(RegSystems, pk=pk)

    if request.method == 'POST':
        form = PostRegSystemsForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostRegSystemsForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def typeregsys_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = TypeRegsys.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(typeid__icontains=query) |
            Q(regsysid__icontains=query) |
            Q(usernameregsys__icontains=query) |
            Q(sysnameregsys__icontains=query) |
            Q(description__icontains=query) |
            Q(ispath__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/typeregsys.html', context)


def typeregsys_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(TypeRegsys, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/typeregsys')
    return render(request, 'tables/typeregsys.html', {'device': obj})


def typeregsys_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/typeregsys_new_post.html'
    form = PostTypeRegsysForm(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись новой системы регистрации по типам ЛА добавлена!')
            form = PostTypeRegsysForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def typeregsys_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/typeregsys_new_post.html'
    post = get_object_or_404(TypeRegsys, pk=pk)

    if request.method == 'POST':
        form = PostTypeRegsysForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostTypeRegsysForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def tasks_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Tasks.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(username__icontains=query) |
            Q(sysname__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/tasks.html', context)


def tasks_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/tasks')
    return render(request, 'tables/tasks.html', {'device': obj})


def tasks_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/tasks_new_post.html'
    form = PostTasksForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись новой базы экспрессов добавлена!')
            form = PostTasksForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def tasks_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/tasks_new_post.html'
    post = get_object_or_404(Tasks, pk=pk)

    if request.method == 'POST':
        form = PostTasksForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostTasksForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def typetasks_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = TypeTasks.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(typeid__icontains=query) |
            Q(taskid__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/typetasks.html', context)


def typetasks_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(TypeTasks, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/typetasks')
    return render(request, 'tables/typetasks.html', {'device': obj})


def typetasks_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/typetasks_new_post.html'
    form = PostTypeTasksForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись новой базы экспресса для типа ЛА назначена!')
            form = PostTypeTasksForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def typetasks_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/typetasks_new_post.html'
    post = get_object_or_404(TypeTasks, pk=pk)

    if request.method == 'POST':
        form = PostTypeTasksForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostTypeTasksForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def misc_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Misc.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(name__icontains=query) |
            Q(sysname__icontains=query) |
            Q(username__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/misc.html', context)


def misc_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Misc, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/misc')
    return render(request, 'tables/misc.html', {'device': obj})


def misc_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/misc_new_post.html'
    form = PostMiscForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового дополнительного элемента типа ЛА, добавлена!!')
            form = PostMiscForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def misc_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/misc_new_post.html'
    post = get_object_or_404(Misc, pk=pk)

    if request.method == 'POST':
        form = PostMiscForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostMiscForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def typemisc_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = TypeMisc.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(typeid__icontains=query) |
            Q(miscid__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/typemisc.html', context)


def typemisc_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(TypeMisc, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/typemisc')
    return render(request, 'tables/typemisc.html', {'device': obj})


def typemisc_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/typemisc_new_post.html'
    form = PostTypeMiscForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового элемента типу ЛА добавлена!')
            form = PostTypeMiscForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def typemisc_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/typemisc_new_post.html'
    post = get_object_or_404(TypeMisc, pk=pk)

    if request.method == 'POST':
        form = PostTypeMiscForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostTypeMiscForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def organisations_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Organisations.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(name__icontains=query) |
            Q(city__icontains=query) |
            Q(notes__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/organisations.html', context)


def organisations_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Organisations, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/organisations')
    return render(request, 'tables/organisations.html', {'device': obj})


def organisations_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/organisations_new_post.html'
    form = PostOrganisationsForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись новой организации-закачкика добавлена!')
            form = PostOrganisationsForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def organisations_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/organisations_new_post.html'
    post = get_object_or_404(Organisations, pk=pk)

    if request.method == 'POST':
        form = PostOrganisationsForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostOrganisationsForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def regsysdevices_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = RegSysDevices.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(regsysid__icontains=query) |
            Q(deviceid__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/regsysdevices.html', context)


def regsysdevices_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(RegSysDevices, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/regsysdevices')
    return render(request, 'tables/regsysdevices.html', {'device': obj})


def regsysdevices_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/regsysdevices_new_post.html'
    form = PostRegSysDevicesForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового соответствия системы регистрации устройств сброса добавлена!')
            form = PostRegSysDevicesForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def regsysdevices_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/regsysdevices_new_post.html'
    post = get_object_or_404(RegSysDevices, pk=pk)

    if request.method == 'POST':
        form = PostRegSysDevicesForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostRegSysDevicesForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def modules_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Modules.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(ispath__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/modules.html', context)


def modules_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Modules, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/modules')
    return render(request, 'tables/modules.html', {'device': obj})


def modules_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/modules_new_post.html'
    form = PostModulesForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового дополнительного модуля входящий в состав ПО СКАТ, добавлена!')
            form = PostModulesForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def modules_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/modules_new_post.html'
    post = get_object_or_404(Modules, pk=pk)

    if request.method == 'POST':
        form = PostModulesForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostModulesForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def drivers_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Drivers.objects.all()
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(name__icontains=query) |
            Q(ispath__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'tables/drivers.html', context)


def drivers_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Drivers, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/tables/drivers')
    return render(request, 'tables/drivers.html', {'device': obj})


def drivers_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/drivers_new_post.html'
    form = PostDriversForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового списка драйверов плат сопряжения и прочих устройств, добавлена!')
            form = PostDriversForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def drivers_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'tables/drivers_new_post.html'
    post = get_object_or_404(Drivers, pk=pk)

    if request.method == 'POST':
        form = PostDriversForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = PostDriversForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def edit_set_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Sets.objects.all()

    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(date__icontains=query) |
            Q(userfriendlyid__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)  # Сколько записей на стрицу отображатся
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,

    }
    return render(request, 'sets/edit_set.html', context)


def edit_set_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Sets, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/edit_set')
    return render(request, 'sets/edit_set.html', {'device': obj})


from django.views.decorators.cache import cache_page


#@cache_page(60 * 15)
def edit_set_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'sets/edit_set_new_post.html'
    form = WidgetForm(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового набора, добавлена!')
            form = WidgetForm()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))
    context = {
        'form': form,
    }
    return render(request, template, context)


#@cache_page(60 * 15)
def edit_set_edit_post(request, userfriendlyid):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'sets/edit_set_new_post.html'
    post = get_object_or_404(Sets, userfriendlyid=userfriendlyid)

    if request.method == 'POST':
        form = WidgetForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = WidgetForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def distrib_list_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj_list = Distribution.objects.all()

    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(name__icontains=query)
            # Q(setid__userfriendlyid=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(obj_list, 20)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
    }
    return render(request, 'distribution/distribution.html', context)


def distrib_list_new_post(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'distribution/distribution_new_post.html'
    form = Distrib(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового набора, добавлена!')
            form = Distrib()
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))
    context = {
        'form': form,
    }
    return render(request, template, context)


def distrib_list_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    template = 'distribution/distribution_new_post.html'
    post = get_object_or_404(Distribution, pk=pk)

    if request.method == 'POST':
        form = Distrib(request.POST, instance=post)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Ошибка: {}'.format(e))

    else:
        form = Distrib(instance=post)

    context = {
        'form': form,
        'post': post,

    }
    return render(request, template, context)


def distrib_list_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    obj = get_object_or_404(Distribution, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/distrib_list')
    return render(request, 'distrib_list/distribution.html', {'device': obj})
