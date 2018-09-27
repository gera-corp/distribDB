from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tables/', views.tables),
    path('programms/', views.programms),
]