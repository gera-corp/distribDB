from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import drop_device, hasp_keys
from .forms import PostForm, PostHaspForm


def home(request):
    return render(request, 'index.html')


def tables(request):
    return render(request, 'tables.html')


def programms(request):
    return render(request, 'programms.html')


def drop_device_view(request):
    obj = drop_device.objects.all()
    query = request.GET.get('q')
    if query:
        obj = obj.filter(SysName__icontains=query)
    return render(request, 'drop_devices.html', {'object_list': obj})


def drop_device_delete(request, id):
    obj = get_object_or_404(drop_device, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/drop_devices')
    return render(request, 'drop_devices.html', {'device': obj})


def new_post(requst):
    template = 'drop_device_new_post.html'
    form = PostForm(requst.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(requst, 'Запись нового устройства добавлена!')
    except Exception as e:
        messages.warning(requst, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(requst, template, context)


def edit_post(request, pk):
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
    obj = hasp_keys.objects.all()
    query = request.GET.get('q')
    if query:
        obj = obj.filter(
            Q(ChipNo__icontains=query) |
            Q(Notes__icontains=query)
        ).distinct()

    return render(request, 'hasp_keys.html', {'object_list': obj})


def hasp_keys_delete(request, id):
    obj = get_object_or_404(hasp_keys, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/hasp_keys')
    return render(request, 'hasp_keys.html', {'device': obj})


def hasp_keys_new_post(requst):
    template = 'hasp_keys_new_post.html'
    form = PostHaspForm(requst.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(requst, 'Запись нового ключа добавлена!')
    except Exception as e:
        messages.warning(requst, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(requst, template, context)


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