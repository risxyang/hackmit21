from django import forms


class UploadForm(forms.Form):
    image_upload = forms.ImageField()
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)