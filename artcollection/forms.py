from django import forms


class UploadForm(forms.Form):
    image_upload = forms.ImageField()
    name = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.IntegerField()