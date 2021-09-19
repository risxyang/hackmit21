from typing import Any, Tuple, Iterator

from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm
from .models import SubmissionModel
import os
from artcollection.models import SubmissionModel

# def index(request):
#     name = request.GET.get("name") or "world"
#     return render(request, "base.html", {"name": name})

def gallery(request):
    path = "media/images/"
    img_list = os.listdir(path)
    print(img_list)
    metadata = []

    for pic in img_list:
        title = pic.split('.')
        val = "images/"+title[0]
        print(val)
        name = SubmissionModel.objects.filter(image_field__startswith = val)[0].name
        city = SubmissionModel.objects.filter(image_field__startswith = val)[0].city
        street = SubmissionModel.objects.filter(image_field__startswith = val)[0].street
        state = SubmissionModel.objects.filter(image_field__startswith = val)[0].state
        zipcode = SubmissionModel.objects.filter(image_field__startswith = val)[0].zip
        metadata.append(",".join([name, city, street, state, str(zipcode)]))

    mylist = zip(img_list, metadata)
    context = {'mylist': mylist}
    return render(request, 'gallery.html', context)

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
        instance.street = form.cleaned_data["street"]
        instance.city = form.cleaned_data["city"]
        instance.state = form.cleaned_data["state"]
        instance.zip = form.cleaned_data["zip"]
        instance.save()
    return render(request, "django_form_upload_art.html", {"form": form, "instance":instance})

