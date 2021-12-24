from rest_framework import serializers
from api.models import CarBrand, CarModel, CarVendor


class CarVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarVendor
        fields = ['company', 'country', 'location', 'latitude', 'longitude', 'telephone', ]


class CarModelSerializer(serializers.ModelSerializer):
    # vendors = CarVendorSerializer(many=True)

    class Meta:
        model = CarModel
        fields = ['name', 'year', 'power', ]


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
            CarModel.objects.create(**data, car=new_car)
        # for vendor in car_model_data:
        #     car_ven = vendor
        #     print(car_ven.pop('vendors'))
        #     CarVendor.objects.create(**vendor, name=car_model_data)
        return new_car
