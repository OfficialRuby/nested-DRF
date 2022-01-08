from tastie.models import SimpleRest, PaystackWebhook
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization


class RestResource(ModelResource):
    class Meta:
        queryset = SimpleRest.objects.all()
        resource_name = 'rest'
        fields = ['name', 'age', 'timestamp', 'data', ]
        authorization = Authorization()


class PaystackResource(ModelResource):
    class Meta:
        queryset = PaystackWebhook.objects.all()
        resource_name = 'paystack'
        fields = ['event',  'data', ]
        authorization = Authorization()
