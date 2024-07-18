from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    added_by = models.CharField(max_length=100)
    people_in_photo = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Photo {self.id}"
