from django.shortcuts import render
import json
from .models import drop_device

# Create your views here.
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

