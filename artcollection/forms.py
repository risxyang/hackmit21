from django import forms


class UploadForm(forms.Form):
    image_upload = forms.ImageField()
    name = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100, help_text="Street")
    city = forms.CharField(max_length=100, help_text="City")
    state = forms.CharField(max_length=100, help_text="State")
    zip = forms.IntegerField(help_text="Zipcode")