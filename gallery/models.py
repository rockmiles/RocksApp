from django.db import models
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images/')
