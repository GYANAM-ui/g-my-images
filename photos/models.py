from django.db import models
from django.db.models.fields import files

# Create your models here.
class Photo(models.Model):
    file = models.FileField(upload_to='file')