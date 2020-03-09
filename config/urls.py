from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.habits, name='habits'),
    path('habit-logs/<int:pk>', views.habit_logs, name='habit_logs'),
    path('add-habit/', views.add_habit, name='add_habit'),
    path('add-log/', views.add_log, name='add_log'),
    path('edit-habit/<int:pk>', views.edit_habit, name='edit_habit'),
    path('edit-log/', views.edit_log, name='edit_log'),
    path('delete-habit/<int:pk>', views.delete_habit, name='delete_habit'),
    path('add-observer/<int:pk>', views.add_observer, name='add_observer'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
