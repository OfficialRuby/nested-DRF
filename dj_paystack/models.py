from django.db import models
# ./manage.py makemigrations && ./manage.py migrate


class Webhook(models.Model):
    event = models.CharField(max_length=50)

    def __str__(self):
        return self.event


class WebhookData(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    data = models.OneToOneField(Webhook, on_delete=models.CASCADE, related_name='data')
    domian = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    gateway_response = models.CharField(max_length=50, blank=True, null=True)
    paid_at = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.CharField(max_length=50, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    metadata = models.CharField(max_length=50, blank=True, null=True)
    fees = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.reference


class WebhookLog(models.Model):
    log = models.OneToOneField(WebhookData, on_delete=models.CASCADE, related_name='log')
    time_spent = models.PositiveIntegerField(blank=True, null=True)
    attempts = models.PositiveIntegerField(blank=True, null=True)
    authentication = models.CharField(max_length=50, blank=True, null=True)
    errors = models.PositiveIntegerField(blank=True, null=True)
    success = models.BooleanField(blank=True, null=True)
    mobile = models.BooleanField(blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.channel


class WebhookInput(models.Model):
    input = models.ManyToManyField(WebhookLog, related_name="input",)


class WebhookHistory(models.Model):
    history = models.ForeignKey(WebhookLog, on_delete=models.CASCADE, related_name="history",)
    type = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    time = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.message


class WebhookCustomer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    customer = models.OneToOneField(WebhookData, on_delete=models.CASCADE, related_name="customer",)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    customer_code = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    metadata = models.CharField(max_length=50, blank=True, null=True)
    risk_action = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.email


class WebhookAuthorization(models.Model):
    authorization = models.OneToOneField(WebhookData, on_delete=models.CASCADE, related_name="authorization",)
    authorization_code = models.CharField(max_length=50, blank=True, null=True)
    bin = models.CharField(max_length=50, blank=True, null=True)
    last4 = models.CharField(max_length=50, blank=True, null=True)
    exp_month = models.CharField(max_length=50, blank=True, null=True)
    exp_year = models.CharField(max_length=50, blank=True, null=True)
    card_type = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    account_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.authorization_code


class WebhookPlan(models.Model):
    plan = models.OneToOneField(WebhookData, on_delete=models.CASCADE, related_name="plan",)
