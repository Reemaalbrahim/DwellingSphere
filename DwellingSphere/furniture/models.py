from django.db import models

class FurnitureShop(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

