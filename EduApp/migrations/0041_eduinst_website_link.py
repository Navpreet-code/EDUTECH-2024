# Generated by Django 5.0.7 on 2024-11-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EduApp", "0040_remove_eduinst_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="eduinst",
            name="Website_Link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
