# Generated by Django 4.0 on 2022-01-06 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_paystack', '0010_remove_webhookhistory_history_webhookhistory_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webhookdata',
            name='customer',
        ),
        migrations.CreateModel(
            name='WebhookCustomer',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_code', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('metadata', models.CharField(blank=True, max_length=50, null=True)),
                ('risk_action', models.CharField(blank=True, max_length=50, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='dj_paystack.webhookdata')),
            ],
        ),
    ]
