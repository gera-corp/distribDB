from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tables/', views.tables),
    path('programms/', views.programms),
    path('drop_devices/', views.drop_device_view),
    path('drop_devices/<int:id>/delete/', views.drop_device_delete, name='drop_device_delete'),
    path('drop_devices/new_post/', views.drop_device_new_post, name='drop_device_new_post'),
    path('drop_devices/edit_post/<int:pk>/', views.drop_device_edit_post, name='drop_device_edit_post'),

    path('hasp_keys/', views.hasp_keys_view),
    path('hasp_keys/<int:id>/delete/', views.hasp_keys_delete, name='hasp_keys_delete'),
    path('hasp_keys/new_post/', views.hasp_keys_new_post, name='hasp_keys_new_post'),
    path('hasp_keys/edit_post/<int:pk>/', views.hasp_keys_edit_post, name='hasp_keys_edit_post'),

    path('hardlock_keys/', views.hardlock_keys_view),
    path('hardlock_keys/<int:id>/delete/', views.hardlock_keys_delete, name='hardlock_keys_delete'),
    path('hardlock_keys/new_post/', views.hardlock_keys_new_post, name='hardlock_keys_new_post'),
    path('hardlock_keys/edit_post/<int:pk>/', views.hardlock_keys_edit_post, name='hardlock_keys_edit_post'),

    path('plane_types/', views.plane_types_view),
    path('plane_types/<int:id>/delete/', views.plane_types_delete, name='plane_types_delete'),
    path('plane_types/new_post/', views.plane_types_new_post, name='plane_types_new_post'),
    path('plane_types/edit_post/<int:pk>/', views.plane_types_edit_post, name='plane_types_edit_post'),

    path('lang_types/', views.lang_types_view),
    path('lang_types/<int:id>/delete/', views.lang_types_delete, name='lang_types_delete'),
    path('lang_types/new_post/', views.lang_types_new_post, name='lang_types_new_post'),
    path('lang_types/edit_post/<int:pk>/', views.lang_types_edit_post, name='lang_types_edit_post'),

    path('os_types/', views.os_types_view),
    path('os_types/<int:id>/delete/', views.os_types_delete, name='os_types_delete'),
    path('os_types/new_post/', views.os_types_new_post, name='os_types_new_post'),
    path('os_types/edit_post/<int:pk>/', views.os_types_edit_post, name='os_types_edit_post'),

]