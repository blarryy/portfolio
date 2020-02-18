from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='projects/')