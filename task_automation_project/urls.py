from django.contrib import admin
from django.urls import path
from automation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('organize/', views.organize_files, name='organize_files'),
]
