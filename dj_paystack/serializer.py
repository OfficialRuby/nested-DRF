from rest_framework import serializers
from dj_paystack.models import (Webhook, WebhookData, WebhookLog, WebhookInput, WebhookHistory,
                                WebhookCustomer, WebhookAuthorization, WebhookPlan)


class WebhookPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebhookPlan
        fields = ['id']


class WebhookAuthorizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebhookAuthorization
        fields = ['authorization_code', 'bin', 'last4', 'exp_month', 'exp_year',
                  'card_type', 'bank', 'country_code', 'brand', 'account_name', ]


class WebhookCustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = WebhookCustomer
        fields = ['id', 'first_name', 'last_name', 'email', 'customer_code', 'phone', 'metadata', 'risk_action', ]


class WebhookHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WebhookHistory
        # fields = ['__all__']
        fields = ['type', 'message', 'time', ]


class WebhookInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebhookInput
        # fields = ['id']


class WebhookLogSerializer(serializers.ModelSerializer):

    class Meta:
        history = WebhookHistorySerializer(many=True)
        input = WebhookInputSerializer(many=True)
        model = WebhookLog
        fields = ['time_spent', 'attempts', 'authentication', 'errors',
                  'success', 'mobile', 'input', 'channel', 'history', ]


class WebhookDataSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    metadata = serializers.IntegerField()
    log = WebhookLogSerializer()
    customer = WebhookCustomerSerializer()
    authorization = WebhookAuthorizationSerializer()
    plan = WebhookPlanSerializer(required=False)

    class Meta:
        model = WebhookData
        fields = ['id', 'domian', 'status', 'reference', 'amount', 'message', 'gateway_response', 'paid_at', 'created_at',
                  'channel', 'currency', 'ip_address', 'metadata', 'log', 'fees', 'customer', 'authorization', 'plan', ]


class WebhookSerializer(serializers.ModelSerializer):
    data = WebhookDataSerializer()

    class Meta:
        model = Webhook
        fields = ['event', 'data', ]

    def create(self, validated_data):
        webhook_data = validated_data.pop('data')
        new_webhook = Webhook.objects.create(**validated_data)
        for data in webhook_data:
            WebhookData.objects.create(**data, data=new_webhook)

        return new_webhook
