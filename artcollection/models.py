from django.db import models

# Create your models here.
class SubmissionModel(models.Model):
    image_field = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)