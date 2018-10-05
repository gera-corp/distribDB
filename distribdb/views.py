from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import drop_device, hasp_keys, hardlock_keys, plane_types, Lang_types, OS_type, executables, FASModules, ExecutablePaths
from .forms import PostForm, PostHaspForm, PostHardlockForm, PostPlaneTypeForm, PostLangForm, PostOsForm, PostExecutablesForm, PostFASModulesForm, PostExecutablePathsForm


def home(request):
    return render(request, 'index.html')


def tables(request):
    return render(request, 'tables.html')


def programms(request):
    return render(request, 'programms.html')


def drop_device_view(request):
    obj_list = drop_device.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
            Q(SysName__icontains=query)
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
    return render(request, 'drop_devices.html', context)


def drop_device_delete(request, id):
    obj = get_object_or_404(drop_device, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/drop_devices')
    return render(request, 'drop_devices.html', {'device': obj})


def drop_device_new_post(request):
    template = 'drop_device_new_post.html'
    form = PostForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового устройства добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def drop_device_edit_post(request, pk):
    template = 'drop_device_new_post.html'
    post = get_object_or_404(drop_device, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Изменения внесены')
        except Exception as e:
            messages.warning(request, 'Изменения не внесены! Шоибка: {}'.format(e))

    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def hasp_keys_view(request):
    obj_list = hasp_keys.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        obj_list = obj_list.filter(
             Q(ChipNo__icontains=query) |
             Q(Notes__icontains=query)
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
    return render(request, 'hasp_keys.html', context)


def hasp_keys_delete(request, id):
    obj = get_object_or_404(hasp_keys, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/hasp_keys')
    return render(request, 'hasp_keys.html', {'device': obj})


def hasp_keys_new_post(request):
    template = 'hasp_keys_new_post.html'
    form = PostHaspForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового ключа добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def hasp_keys_edit_post(request, pk):
    template = 'hasp_keys_new_post.html'
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
    obj = hardlock_keys.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(ChipNo__icontains=query) |
            Q(Notes__icontains=query)
        ).distinct()

    return render(request, 'hardlock_keys.html', {'object_list': obj})


def hardlock_keys_delete(request, id):
    obj = get_object_or_404(hardlock_keys, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/hardlock_keys')
    return render(request, 'hardlock_keys.html', {'device': obj})


def hardlock_keys_new_post(request):
    template = 'hardlock_keys_new_post.html'
    form = PostHardlockForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового ключа добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def hardlock_keys_edit_post(request, pk):
    template = 'hardlock_keys_new_post.html'
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
    obj = plane_types.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(SysName__icontains=query) |
            Q(UserName__icontains=query) |
            Q(Description__icontains=query)
        ).distinct()

    return render(request, 'plane_types.html', {'object_list': obj})


def plane_types_delete(request, id):
    obj = get_object_or_404(plane_types, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/plane_types')
    return render(request, 'plane_types.html', {'device': obj})


def plane_types_new_post(request):
    template = 'plane_types_new_post.html'
    form = PostPlaneTypeForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового типа добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def plane_types_edit_post(request, pk):
    template = 'plane_types_new_post.html'
    post = get_object_or_404(plane_types, pk=pk)

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
    obj = Lang_types.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(Lang__icontains=query) |
            Q(Lcode__icontains=query) |
            Q(ISDefine__icontains=query)
        ).distinct()

    return render(request, 'lang_types.html', {'object_list': obj})


def lang_types_delete(request, id):
    obj = get_object_or_404(Lang_types, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/lang_types')
    return render(request, 'lang_types.html', {'device': obj})


def lang_types_new_post(request):
    template = 'lang_types_new_post.html'
    form = PostLangForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового языка добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def lang_types_edit_post(request, pk):
    template = 'lang_types_new_post.html'
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
    obj = OS_type.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(OS__icontains=query) |
            Q(OSCode__icontains=query)
        ).distinct()

    return render(request, 'os_types.html', {'object_list': obj})


def os_types_delete(request, id):
    obj = get_object_or_404(OS_type, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/os_types')
    return render(request, 'os_types.html', {'device': obj})


def os_types_new_post(request):
    template = 'os_types_new_post.html'
    form = PostOsForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись новой OS добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def os_types_edit_post(request, pk):
    template = 'os_types_new_post.html'
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
    obj = executables.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(FileName__icontains=query)
        ).distinct()

    return render(request, 'executables.html', {'object_list': obj})


def executables_delete(request, id):
    obj = get_object_or_404(executables, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/executables')
    return render(request, 'executables.html', {'device': obj})


def executables_new_post(request):
    template = 'executables_new_post.html'
    form = PostExecutablesForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового модуля добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def executables_edit_post(request, pk):
    template = 'executables_new_post.html'
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
    obj = FASModules.objects.all()
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(ExecutableID__icontains=query)
        ).distinct()

    return render(request, 'fas_modules.html', {'object_list': obj})


def fas_modules_delete(request, id):
    obj = get_object_or_404(FASModules, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/fas_modules')
    return render(request, 'fas_modules.html', {'device': obj})


def fas_modules_new_post(request):
    template = 'fas_modules_new_post.html'
    form = PostFASModulesForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового номера FAS добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def fas_modules_edit_post(request, pk):
    template = 'fas_modules_new_post.html'
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
    obj = ExecutablePaths.objects.all()
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(ExecutableID__icontains=query)
        ).distinct()

    return render(request, 'executable_paths.html', {'object_list': obj})


def executable_paths_delete(request, id):
    obj = get_object_or_404(ExecutablePaths, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/executable_paths')
    return render(request, 'executable_paths.html', {'device': obj})


def executable_paths_new_post(request):
    template = 'executable_paths_new_post.html'
    form = PostExecutablePathsForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись нового пути InstallShield добавлена!')
    except Exception as e:
        messages.warning(request, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)


def executable_paths_edit_post(request, pk):
    template = 'executable_paths_new_post.html'
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