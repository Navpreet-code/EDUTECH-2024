# Generated by Django 5.0.7 on 2024-11-05 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EduApp", "0034_eduinst_address_eduinst_email_eduinst_phoneno_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eduinst",
            old_name="Title",
            new_name="Titles",
        ),
    ]
