from rest_framework import serializers
from api.models import CarBrand, CarModel, CarVendor


class CarVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarVendor
        fields = ['company', 'country', 'location', 'latitude', 'longitude', 'telephone', ]


class CarModelSerializer(serializers.ModelSerializer):
    vendors = CarVendorSerializer(many=True)

    class Meta:
        model = CarModel
        fields = ['name', 'year', 'power', 'vendors']


class CarBrandSerializer(serializers.ModelSerializer):
    models = CarModelSerializer(many=True)

    class Meta:
        model = CarBrand
        fields = ['make', 'models']

    def create(self, validated_data):
        car_model_data = validated_data.pop('models')
        new_car = CarBrand.objects.create(**validated_data)
        # Loop through items in car model data and create car details
        for data in car_model_data:
            x = 0
            car_vendor = data.pop('vendors')
            print('\n\n')
            # print(item)
            print(data)
            print('\n\n')
            print(data)
            print('\n\n')
            CarModel.objects.create(**data, car=new_car)
            # CarVendor.objects.create(*car_vendor,)
        for item in range(len(car_vendor)):
            print('\n\n')
            print(item)
            print(data)
            print('\n\n')
            CarVendor.objects.create(**car_vendor[item],)

        # for vendor in car_model_data:
        #     print(vendor)
        #     car_ven = vendor
        #     CarVendor.objects.create(**vendor, name=car_model_data)
        return new_car
