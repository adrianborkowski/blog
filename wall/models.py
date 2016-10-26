from django.db import models
from gdstorage.storage import GoogleDriveStorage


# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts', storage=gd_storage)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


