
from django.contrib import admin
from django.urls import path, include
from api.views import CarBrandView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/car/', CarBrandView.as_view(), name='api')
]
