from django.contrib import admin
from projects.models import Project
from projects.models import Technology
from django.db import models

class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'technologies', 'github', 'production')

class TechnologyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
