# Generated by Django 5.0.7 on 2024-09-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EduApp", "0019_rename_stat_statistic_statistic_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="statistic_detail",
            name="Statistic",
        ),
        migrations.RemoveField(
            model_name="statistic_detail",
            name="Title",
        ),
        migrations.RemoveField(
            model_name="statistic_detail",
            name="Year",
        ),
        migrations.RemoveField(
            model_name="statistic_detail",
            name="id",
        ),
        migrations.RemoveField(
            model_name="statistic_detail",
            name="pdf",
        ),
        migrations.AddField(
            model_name="statistic_detail",
            name="State",
            field=models.CharField(
                default=1, max_length=1000, primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="statistic_detail",
            name="State_Image",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
    ]
