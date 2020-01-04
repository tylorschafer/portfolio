from django.contrib import admin
from projects.models import Project
from django.db import models

class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'technology')

admin.site.register(Project, ProjectAdmin)
