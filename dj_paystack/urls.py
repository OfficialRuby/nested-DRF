from django.urls import path
from dj_paystack.views import WebhookView

urlpatterns = [
    path('verify/', WebhookView.as_view(), name='verify ')
]
