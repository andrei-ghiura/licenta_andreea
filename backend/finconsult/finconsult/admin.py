
from django.contrib import admin

from .models import Profile, Meeting


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]


admin.site.register(Profile, ProfileAdmin)


class MeetingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Meeting._meta.get_fields()]


admin.site.register(Meeting, MeetingAdmin)
