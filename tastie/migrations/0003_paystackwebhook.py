# Generated by Django 4.0 on 2022-01-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tastie', '0002_simplerest_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaystackWebhook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50)),
                ('data', models.JSONField()),
            ],
        ),
    ]