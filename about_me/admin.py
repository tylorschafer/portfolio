from django.contrib import admin
from about_me.models import AboutMe

class AboutMeAdmin(admin.ModelAdmin):
    pass

admin.site.register(AboutMe, AboutMeAdmin)
