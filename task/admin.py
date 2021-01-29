from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'user')
    list_display = ('title', 'description', 'created_at', 'updated_at', 'user')

admin.site.register(Task, TaskAdmin)
