from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='news_create'),
    path('<slug:slug>', views.NewsDetailView.as_view(), name='NewsDetailView'),
    path('<slug:slug>/update', views.NewsUpdateView, name='NewsUpdateView'),
    path('<slug:slug>/delete', views.NewsDeleteView.as_view(), name='NewsDeleteView')
]