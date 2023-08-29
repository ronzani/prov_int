# Generated by Django 4.2.4 on 2023-08-29 13:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_alter_cidade_estado"),
    ]

    operations = [
        migrations.AddField(
            model_name="cidade",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True, verbose_name="uuid"),
        ),
        migrations.AddField(
            model_name="estado",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True, verbose_name="uuid"),
        ),
    ]
