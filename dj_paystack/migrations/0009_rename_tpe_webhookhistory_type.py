# Generated by Django 4.0 on 2022-01-06 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_paystack', '0008_rename_type_webhookhistory_tpe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webhookhistory',
            old_name='tpe',
            new_name='type',
        ),
    ]
