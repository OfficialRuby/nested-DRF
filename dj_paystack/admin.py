from django.contrib import admin
from dj_paystack.models import (Webhook, WebhookData, WebhookLog, WebhookHistory, WebhookCustomer,
                                WebhookAuthorization)
# Register your models here.

admin.site.register(Webhook)
admin.site.register(WebhookData)
admin.site.register(WebhookLog)
admin.site.register(WebhookHistory)
admin.site.register(WebhookCustomer)
admin.site.register(WebhookAuthorization)
