# Generated by Django 5.0.7 on 2024-08-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EduApp", "0009_alter_article_description_alter_article_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="college",
            name="PhoneNo",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="universitie",
            name="PhoneNo",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
