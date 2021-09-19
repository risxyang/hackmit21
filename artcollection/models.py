from django.db import models

# Create your models here.
class SubmissionModel(models.Model):
    image_field = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100, help_text= "A descriptive name")
    street = models.CharField(max_length=100, help_text="Street")
    city = models.CharField(max_length=100, help_text="City")
    state = models.CharField(max_length=100, help_text="State")
    zip = models.IntegerField(help_text="Zipcode", default=0)