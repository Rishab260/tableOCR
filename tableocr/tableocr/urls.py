# project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from image_processor_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.upload_image),
]