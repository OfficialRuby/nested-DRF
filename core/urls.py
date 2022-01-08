
from django.contrib import admin
from django.urls import path, include
from api.views import CarBrandView
from tastie.api import RestResource, PaystackResource

rest_resource = RestResource()
paystack_resource = PaystackResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('dj_paystack.urls')),
    path('api/', include(rest_resource.urls)),
    path('api/', include(paystack_resource.urls)),
    path('api/car/', CarBrandView.as_view(), name='api')
]
