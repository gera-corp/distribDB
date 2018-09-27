from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def tables(request):
    return render(request, 'tables.html')

def programms(request):
    return render(request, 'programms.html')
