from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import drop_device
from .forms import PostForm


def home(request):
    return render(request, 'index.html')


def tables(request):
    return render(request, 'tables.html')


def programms(request):
    return render(request, 'programms.html')


def drop_device_view(request):
    obj = drop_device.objects.all()
    return render(request, 'drop_devices.html', {'object_list': obj})


def drop_device_delete(request, id):
    odj = get_object_or_404(drop_device, id=id)
    if request.method == 'POST':
        odj.delete()
        return redirect('/drop_devices/')
    return render(request, 'drop_devices.html', {'device': odj})


def new_post(requst):
    template = 'new_post.html'
    form = PostForm(requst.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(requst, 'Запись нового устройства добавлена!')

            #return redirect('/drop_devices/')
    except Exception as e:
        form = PostForm()
        messages.warning(requst, 'Запись не была добавлена! Ошибка: {}'.format(e))

    context = {
        'form': form,
    }
    return render(requst, template, context)