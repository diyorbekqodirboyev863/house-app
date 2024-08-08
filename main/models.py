from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# House.
class House(models.Model):
    HOUSE_TYPE = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('unknown', 'Unknown')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    house_type = models.CharField(max_length=10, choices=HOUSE_TYPE, default='sale')
    location = models.CharField(max_length=255)
    location_URL = models.URLField(blank=True, null=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.IntegerField()
    posted_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.title = self.title.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Image(models.Model):
    house = models.ForeignKey(to=House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.house.title} - {self.id}"