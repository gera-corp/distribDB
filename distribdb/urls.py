from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tables/', views.tables),
    path('programms/', views.programms),
    path('drop_devices/', views.drop_device_view),
    path('drop_devices/<int:id>/delete/', views.drop_device_delete, name='delete'),
    path('drop_devices/new_post/', views.new_post, name='new_post'),
    path('drop_devices/edit_post/<int:pk>/', views.edit_post, name='edit_post'),
]