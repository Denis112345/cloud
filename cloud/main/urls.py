from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url
from .views import *
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='indexView'),
    path('upload/', DocumentUpload, name='document_upload'),
    path('documentAll/', DocumentAll, name='documentAll'),
    path('documentAll/<slug:slug>', DocumentDownload, name='documentDownload'),
    path('documentAll/<slug:slug>/detail', DocumentDetailView.as_view(), name='document_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()