# Generated by Django 5.0.7 on 2024-08-22 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EduApp", "0007_articles_colleges_laws_universities"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Articles",
            new_name="Article",
        ),
        migrations.RenameModel(
            old_name="Colleges",
            new_name="College",
        ),
        migrations.RenameModel(
            old_name="laws",
            new_name="law",
        ),
        migrations.RenameModel(
            old_name="Universities",
            new_name="Universitie",
        ),
    ]
