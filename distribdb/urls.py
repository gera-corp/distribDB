from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('programms/', views.programms),
    path('tables/', views.tables),

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

    path('executables/', views.executables_view),
    path('executables/<int:id>/delete/', views.executables_delete, name='executables_delete'),
    path('executables/new_post/', views.executables_new_post, name='executables_new_post'),
    path('executables/edit_post/<int:pk>/', views.executables_edit_post, name='executables_edit_post'),

    path('fas_modules/', views.fas_modules_view),
    path('fas_modules/<int:id>/delete/', views.fas_modules_delete, name='fas_modules_delete'),
    path('fas_modules/new_post/', views.fas_modules_new_post, name='fas_modules_new_post'),
    path('fas_modules/edit_post/<int:pk>/', views.fas_modules_edit_post, name='fas_modules_edit_post'),

    path('executable_paths/', views.executable_paths_view),
    path('executable_paths/<int:id>/delete/', views.executable_paths_delete, name='executable_paths_delete'),
    path('executable_paths/new_post/', views.executable_paths_new_post, name='executable_paths_new_post'),
    path('executable_paths/edit_post/<int:pk>/', views.executable_paths_edit_post, name='executable_paths_edit_post'),

    path('regsystems/', views.regsystems_view),
    path('regsystems/<int:id>/delete/', views.regsystems_delete, name='regsystems_delete'),
    path('regsystems/new_post/', views.regsystems_new_post, name='regsystems_new_post'),
    path('regsystems/edit_post/<int:pk>/', views.regsystems_edit_post, name='regsystems_edit_post'),

    path('typeregsys/', views.typeregsys_view),
    path('typeregsys/<int:id>/delete/', views.typeregsys_delete, name='typeregsys_delete'),
    path('typeregsys/new_post/', views.typeregsys_new_post, name='typeregsys_new_post'),
    path('typeregsys/edit_post/<int:pk>/', views.typeregsys_edit_post, name='typeregsys_edit_post'),

    path('tasks/', views.tasks_view),
    path('tasks/<int:id>/delete/', views.tasks_delete, name='tasks_delete'),
    path('tasks/new_post/', views.tasks_new_post, name='tasks_new_post'),
    path('tasks/edit_post/<int:pk>/', views.tasks_edit_post, name='tasks_edit_post'),

    path('typetasks/', views.typetasks_view),
    path('typetasks/<int:id>/delete/', views.typetasks_delete, name='typetasks_delete'),
    path('typetasks/new_post/', views.typetasks_new_post, name='typetasks_new_post'),
    path('typetasks/edit_post/<int:pk>/', views.typetasks_edit_post, name='typetasks_edit_post'),

    path('misc/', views.misc_view),
    path('misc/<int:id>/delete/', views.misc_delete, name='misc_delete'),
    path('misc/new_post/', views.misc_new_post, name='misc_new_post'),
    path('misc/edit_post/<int:pk>/', views.misc_edit_post, name='misc_edit_post'),

    path('typemisc/', views.typemisc_view),
    path('typemisc/<int:id>/delete/', views.typemisc_delete, name='typemisc_delete'),
    path('typemisc/new_post/', views.typemisc_new_post, name='typemisc_new_post'),
    path('typemisc/edit_post/<int:pk>/', views.typemisc_edit_post, name='typemisc_edit_post'),

    path('organisations/', views.organisations_view),
    path('organisations/<int:id>/delete/', views.organisations_delete, name='organisations_delete'),
    path('organisations/new_post/', views.organisations_new_post, name='organisations_new_post'),
    path('organisations/edit_post/<int:pk>/', views.organisations_edit_post, name='organisations_edit_post'),

    path('regsysdevices/', views.regsysdevices_view),
    path('regsysdevices/<int:id>/delete/', views.regsysdevices_delete, name='regsysdevices_delete'),
    path('regsysdevices/new_post/', views.regsysdevices_new_post, name='regsysdevices_new_post'),
    path('regsysdevices/edit_post/<int:pk>/', views.regsysdevices_edit_post, name='regsysdevices_edit_post'),

    path('modules/', views.modules_view),
    path('modules/<int:id>/delete/', views.modules_delete, name='modules_delete'),
    path('modules/new_post/', views.modules_new_post, name='modules_new_post'),
    path('modules/edit_post/<int:pk>/', views.modules_edit_post, name='modules_edit_post'),

    path('drivers/', views.drivers_view),
    path('drivers/<int:id>/delete/', views.drivers_delete, name='drivers_delete'),
    path('drivers/new_post/', views.drivers_new_post, name='drivers_new_post'),
    path('drivers/edit_post/<int:pk>/', views.drivers_edit_post, name='drivers_edit_post'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]