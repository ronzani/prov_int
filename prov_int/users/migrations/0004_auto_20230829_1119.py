from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_populate_uuid_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="uuid"),
        ),
    ]
