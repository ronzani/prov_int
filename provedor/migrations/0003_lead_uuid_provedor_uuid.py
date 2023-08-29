# Generated by Django 4.2.4 on 2023-08-29 13:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('provedor', '0002_rename_bonuspago_lead_bonus_pago_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid'),
        ),
        migrations.AddField(
            model_name='provedor',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid'),
        ),
    ]
