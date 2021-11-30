from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    science_image = models.ImageField(null= True, blank=True, upload_to = 'images/')
    def __str__(self):
        return self.title