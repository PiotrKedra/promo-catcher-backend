from django.db import models


class Restaurant(models.Model):
    restaurant_name = models.CharField(unique=True, max_length=50)
    data_posted = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(default=None, blank=True, null=True)
    longitude = models.FloatField(default=None, blank=True, null=True)
    facebook_id = models.IntegerField(default=None, blank=True, null=True)
    restaurant_url = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.restaurant_name


class Promotion(models.Model):
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    data_posted = models.DateTimeField(auto_now_add=True)
    data_start = models.DateField(default=None, blank=True, null=True)
    data_end = models.DateField(default=None, blank=True, null=True)
    promotion_message = models.TextField(default=None, blank=True, null=True)
    promotion_name = models.CharField(max_length=100, default='Promocja')

    def __str__(self):
        return f'{self.restaurant_name}: {self.promotion_name} -> {self.promotion_message}'

