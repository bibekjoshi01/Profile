from django.contrib import admin
from .models import Profile, Hobbies


# Register your models here.

class HobbiesInline(admin.TabularInline):
    model = Hobbies


class ProfileModelAdmin(admin.ModelAdmin):
    inlines = [HobbiesInline]


admin.site.register(Profile, ProfileModelAdmin)
