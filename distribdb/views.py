from django.shortcuts import render, get_object_or_404, redirect
from .models import drop_device


def home(request):
    return render(request, 'index.html')


def tables(request):
    return render(request, 'tables.html')


def programms(request):
    return render(request, 'programms.html')


def drop_device_view(request):
    obj = drop_device.objects.all()
    context = {
        'object_list': obj
    }
    return render(request, 'drop_devices.html', context)


def delete(request, id):
    odj = get_object_or_404(drop_device, id=id)
    if request.method == 'POST':
        odj.delete()
        return redirect('/drop_devices/')
    return render(request, 'drop_devices.html', {'device': odj})


