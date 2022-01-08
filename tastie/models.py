from django.db import models


class SimpleRest(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return self.name


class PaystackWebhook(models.Model):
    event = models.CharField(max_length=50)
    data = models.JSONField()

    def __str__(self):
        return self.event
