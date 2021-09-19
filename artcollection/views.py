from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm
from .models import SubmissionModel
import os


def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})

def search(request):
    city = request.GET.get("search")
    return render(request, "search_results.html", {"city": city})

def upload(request):
    if request.method == 'POST':
        save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file_upload"].name)
        with open(save_path, "wb") as output_file:
            for chunk in request.FILES["file_upload"].chunks():
                output_file.write(chunk)
    return render(request, "upload_art.html")

def upload_form(request):
    instance = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
    else:
        form = UploadForm()
    if form.is_valid():
        instance = SubmissionModel()
        instance.image_field = form.cleaned_data["image_upload"]
        instance.name = form.cleaned_data["name"]
        instance.name = form.cleaned_data["address"]
        instance.save()
    return render(request, "django_form_upload_art.html", {"form": form, "instance":instance})
