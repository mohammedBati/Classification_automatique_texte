from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    #title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='')
    #cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title
