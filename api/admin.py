from django.contrib import admin

from api.models import CarBrand, CarModel, CarVendor


admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(CarVendor)
