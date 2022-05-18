from django.contrib import admin

from objectives.models import Objective
# Register your models here.

class ObjectiveAdmin(admin.ModelAdmin):
    pass

admin.site.register(Objective, ObjectiveAdmin)