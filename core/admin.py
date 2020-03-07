from django.contrib import admin

from .models import Habit, Log, Observer


admin.site.register(Habit)
admin.site.register(Log)
admin.site.register(Observer)
