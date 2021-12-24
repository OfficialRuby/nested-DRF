from django.db import models

POWER_CHOICES = (
    ('Internal Combustion Engine', 'Internal Combustion Engine'),
    ('Electric Drive', 'Electric Drive'),
    ('Hybrid Drive', 'Hybrid Drive')
)


class CarBrand(models.Model):
    make = models.CharField(max_length=50)

    def __str__(self):
        return self.make


class CarModel(models.Model):
    car = models.ForeignKey("api.CarBrand", related_name='models', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    year = models.DateField()
    power = models.CharField(max_length=50, choices=POWER_CHOICES)

    def __str__(self):
        return self.name


class CarVendor(models.Model):
    name = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='vendors')
    company = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)

    def __str__(self):
        return self.company
