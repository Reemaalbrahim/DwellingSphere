from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    size = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

