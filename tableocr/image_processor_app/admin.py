
# Register your models here.
# image_processor_app/admin.py
from django.contrib import admin
from .models import UploadedImage

admin.site.register(UploadedImage)
