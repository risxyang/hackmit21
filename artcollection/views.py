from typing import Any, Tuple, Iterator

from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm
from .models import SubmissionModel
import os
import requests
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
        val = "images/" + title[0]
        print(val)
        name = SubmissionModel.objects.filter(image_field__startswith=val)[0].name
        city = SubmissionModel.objects.filter(image_field__startswith=val)[0].city
        street = SubmissionModel.objects.filter(image_field__startswith=val)[0].street
        state = SubmissionModel.objects.filter(image_field__startswith=val)[0].state
        zipcode = SubmissionModel.objects.filter(image_field__startswith=val)[0].zip
        metadata.append(", ".join([name, city, street, state, str(zipcode)]))

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
    return render(request, "django_form_upload_art.html", {"form": form, "instance": instance})


def map(request):
    name = request.GET.get("name") or "world"
    address_elements = SubmissionModel.objects.values_list('street', 'city', 'state')
    latlong_list = []
    for i in range(len(address_elements)):
        address = address_elements[i][0] + ", " + address_elements[i][1] + ", " + address_elements[i][2]
        params = {
            "key": 'AIzaSyDf_9RiBvP-mX5qmEgyUa02k2F8l4TnsU4',
            "address": address
        }
        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        response = requests.get(base_url, params=params).json()
        if response['status'] == 'OK':
            latlong_list.append((response['results'][0]["geometry"]["location"]["lat"],
                                 response['results'][0]["geometry"]["location"]["lng"]))

    base_url_marker = 'https://maps.googleapis.com/maps/api/staticmap?zoom=12&size=800x800&'
    ending = 'key=AIzaSyDf_9RiBvP-mX5qmEgyUa02k2F8l4TnsU4'
    individual_marker = "markers=color:blue%7Clabel:S%7C"
    location = ""
    for i in range(len(latlong_list)):
        location += individual_marker
        location += str(latlong_list[i][0]) + "," + str(latlong_list[i][1])
        location += "&"

    return render(request, "map.html", {"marker": base_url_marker + location + ending})
