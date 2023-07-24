# image_processor_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from . import image_processing





#django code
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            csv_file_path = image_processing.final(image.image.path, output_dir='temp_output', show_table=False)
            with open(csv_file_path, 'r') as csv_file:
                response = HttpResponse(csv_file, content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{csv_file_path.split("/")[-1]}"'
                return response
    else:
        form = UploadImageForm()

    context = {
        'form': form,
    }
    return render(request, 'image_processor_app/upload_image.html', context)