from django.contrib import admin
from .models import Document

# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("descriptions",)}

admin.site.register(Document, DocumentAdmin)



