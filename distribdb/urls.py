from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.home),
    path('programms/', views.programms),
    path('tables/', views.tables),

    path('tables/drop_devices/', views.drop_device_view),
    path('tables/drop_devices/<int:id>/delete/', views.drop_device_delete, name='drop_device_delete'),
    path('tables/drop_devices/new_post/', views.drop_device_new_post),
    path('tables/drop_devices/edit_post/<int:pk>/', views.drop_device_edit_post, name='drop_device_edit_post'),

    path('tables/hasp_keys/', views.hasp_keys_view),
    path('tables/hasp_keys/<int:id>/delete/', views.hasp_keys_delete, name='hasp_keys_delete'),
    path('tables/hasp_keys/new_post/', views.hasp_keys_new_post),
    path('tables/hasp_keys/edit_post/<int:pk>/', views.hasp_keys_edit_post, name='hasp_keys_edit_post'),

    path('tables/hardlock_keys/', views.hardlock_keys_view),
    path('tables/hardlock_keys/<int:id>/delete/', views.hardlock_keys_delete, name='hardlock_keys_delete'),
    path('tables/hardlock_keys/new_post/', views.hardlock_keys_new_post),
    path('tables/hardlock_keys/edit_post/<int:pk>/', views.hardlock_keys_edit_post, name='hardlock_keys_edit_post'),

    path('tables/plane_types/', views.plane_types_view),
    path('tables/plane_types/<int:id>/delete/', views.plane_types_delete, name='plane_types_delete'),
    path('tables/plane_types/new_post/', views.plane_types_new_post),
    path('tables/plane_types/edit_post/<int:pk>/', views.plane_types_edit_post, name='plane_types_edit_post'),

    path('tables/lang_types/', views.lang_types_view),
    path('tables/lang_types/<int:id>/delete/', views.lang_types_delete, name='lang_types_delete'),
    path('tables/lang_types/new_post/', views.lang_types_new_post),
    path('tables/lang_types/edit_post/<int:pk>/', views.lang_types_edit_post, name='lang_types_edit_post'),

    path('tables/os_types/', views.os_types_view),
    path('tables/os_types/<int:id>/delete/', views.os_types_delete, name='os_types_delete'),
    path('tables/os_types/new_post/', views.os_types_new_post),
    path('tables/os_types/edit_post/<int:pk>/', views.os_types_edit_post, name='os_types_edit_post'),

    path('tables/executables/', views.executables_view),
    path('tables/executables/<int:id>/delete/', views.executables_delete, name='executables_delete'),
    path('tables/executables/new_post/', views.executables_new_post),
    path('tables/executables/edit_post/<int:pk>/', views.executables_edit_post, name='executables_edit_post'),

    path('tables/fas_modules/', views.fas_modules_view),
    path('tables/fas_modules/<int:id>/delete/', views.fas_modules_delete, name='fas_modules_delete'),
    path('tables/fas_modules/new_post/', views.fas_modules_new_post),
    path('tables/fas_modules/edit_post/<int:pk>/', views.fas_modules_edit_post, name='fas_modules_edit_post'),

    path('tables/executable_paths/', views.executable_paths_view),
    path('tables/executable_paths/<int:id>/delete/', views.executable_paths_delete, name='executable_paths_delete'),
    path('tables/executable_paths/new_post/', views.executable_paths_new_post),
    path('tables/executable_paths/edit_post/<int:pk>/', views.executable_paths_edit_post, name='executable_paths_edit_post'),

    path('tables/regsystems/', views.regsystems_view),
    path('tables/regsystems/<int:id>/delete/', views.regsystems_delete, name='regsystems_delete'),
    path('tables/regsystems/new_post/', views.regsystems_new_post),
    path('tables/regsystems/edit_post/<int:pk>/', views.regsystems_edit_post, name='regsystems_edit_post'),

    path('tables/typeregsys/', views.typeregsys_view),
    path('tables/typeregsys/<int:id>/delete/', views.typeregsys_delete, name='typeregsys_delete'),
    path('tables/typeregsys/new_post/', views.typeregsys_new_post),
    path('tables/typeregsys/edit_post/<int:pk>/', views.typeregsys_edit_post, name='typeregsys_edit_post'),

    path('tables/tasks/', views.tasks_view),
    path('tables/tasks/<int:id>/delete/', views.tasks_delete, name='tasks_delete'),
    path('tables/tasks/new_post/', views.tasks_new_post),
    path('tables/tasks/edit_post/<int:pk>/', views.tasks_edit_post, name='tasks_edit_post'),

    path('tables/typetasks/', views.typetasks_view),
    path('tables/typetasks/<int:id>/delete/', views.typetasks_delete, name='typetasks_delete'),
    path('tables/typetasks/new_post/', views.typetasks_new_post),
    path('tables/typetasks/edit_post/<int:pk>/', views.typetasks_edit_post, name='typetasks_edit_post'),

    path('tables/misc/', views.misc_view),
    path('tables/misc/<int:id>/delete/', views.misc_delete, name='misc_delete'),
    path('tables/misc/new_post/', views.misc_new_post),
    path('tables/misc/edit_post/<int:pk>/', views.misc_edit_post, name='misc_edit_post'),

    path('tables/typemisc/', views.typemisc_view),
    path('tables/typemisc/<int:id>/delete/', views.typemisc_delete, name='typemisc_delete'),
    path('tables/typemisc/new_post/', views.typemisc_new_post),
    path('tables/typemisc/edit_post/<int:pk>/', views.typemisc_edit_post, name='typemisc_edit_post'),

    path('tables/organisations/', views.organisations_view),
    path('tables/organisations/<int:id>/delete/', views.organisations_delete, name='organisations_delete'),
    path('tables/organisations/new_post/', views.organisations_new_post),
    path('tables/organisations/edit_post/<int:pk>/', views.organisations_edit_post, name='organisations_edit_post'),

    path('tables/regsysdevices/', views.regsysdevices_view),
    path('tables/regsysdevices/<int:id>/delete/', views.regsysdevices_delete, name='regsysdevices_delete'),
    path('tables/regsysdevices/new_post/', views.regsysdevices_new_post),
    path('tables/regsysdevices/edit_post/<int:pk>/', views.regsysdevices_edit_post, name='regsysdevices_edit_post'),

    path('tables/modules/', views.modules_view),
    path('tables/modules/<int:id>/delete/', views.modules_delete, name='modules_delete'),
    path('tables/modules/new_post/', views.modules_new_post),
    path('tables/modules/edit_post/<int:pk>/', views.modules_edit_post, name='modules_edit_post'),

    path('tables/drivers/', views.drivers_view),
    path('tables/drivers/<int:id>/delete/', views.drivers_delete, name='drivers_delete'),
    path('tables/drivers/new_post/', views.drivers_new_post),
    path('tables/drivers/edit_post/<int:pk>/', views.drivers_edit_post, name='drivers_edit_post'),

    path('edit_set/', views.edit_set_view),
    path('edit_set/<int:pk>/delete/', views.edit_set_delete, name='edit_set_delete'),
    path('edit_set/new_post/', views.edit_set_new_post),
    path('edit_set/edit_post/<int:pk>/', views.edit_set_edit_post, name='edit_set_edit_post'),

    # path('edit_set', views.PersonListView.as_view(), name='person_changelist'),
    # path('edit_set/add/', views.PersonCreateView.as_view(), name='person_add'),
    # path('edit_set/<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    # path('edit_set/ajax/', views.load_cities, name='ajax_load_cities'),  # <-- this one here


    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]