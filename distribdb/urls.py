from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tables/', views.tables),
    path('programms/', views.programms),
    path('drop_devices/', views.drop_device_view),
]