# Generated by Django 5.0.7 on 2024-11-04 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EduApp", "0031_eduinst"),
    ]

    operations = [
        migrations.AddField(
            model_name="eduinst",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="eduinst",
            name="Name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="EduApp.course"
            ),
        ),
    ]
