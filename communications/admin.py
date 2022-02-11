from django.contrib import admin
from .models import *

# Register your models here.

class ComAdmin(admin.ModelAdmin):
    list_display = ('subject', 'uuid')

admin.site.register(Cummunication, ComAdmin)
