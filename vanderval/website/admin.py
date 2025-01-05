from django.contrib import admin
from .models import Site, TaskLog, UserRecords

admin.site.register(Site)
admin.site.register(UserRecords)

@admin.register(TaskLog)
class TaskLogAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status', 'started_at', 'finished_at', 'error_message')
    search_fields = ('task_name', 'status')
    list_filter = ('status',)