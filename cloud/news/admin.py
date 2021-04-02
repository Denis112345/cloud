from django.contrib import admin
from .models import Artiсles

# Register your models here.

class ArtiсlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title": ("title",)}

admin.site.register(Artiсles, ArtiсlesAdmin)