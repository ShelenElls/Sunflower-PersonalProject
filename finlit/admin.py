from django.contrib import admin
from finlit.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)