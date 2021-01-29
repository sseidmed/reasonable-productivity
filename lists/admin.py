from django.contrib import admin

from .models import List

class ListAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'user')
    list_display = ('name', 'description', 'created_at', 'updated_at', 'user_id')

admin.site.register(List, ListAdmin)

