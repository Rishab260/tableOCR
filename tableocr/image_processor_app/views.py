# image_processor_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from image_processor_app.forms import UploadImageForm
from . import image_processing
import os

#django code
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                image = form.save()
                csv_file_path = image_processing.final(image.image.path, output_dir='temp_output', show_table=False)
                with open(csv_file_path, 'r') as csv_file:
                    response = HttpResponse(csv_file, content_type='text/csv')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_file_path)}"'
                    os.remove(csv_file_path)
                    return response
            except Exception as e:
                # Handle exceptions here
                return HttpResponse(f"Error processing the image: {e}")
    else:
        form = UploadImageForm()

    context = {
        'form': form,
    }
    return render(request, 'image_processor_app/upload_image.html', context)
