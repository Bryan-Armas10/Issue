from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "name", "summary", "reporter", "assignee", "created_on" 
    ]

    admin_site.register(Issue, IssueAdmin)