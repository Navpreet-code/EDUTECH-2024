# Generated by Django 5.0.7 on 2024-11-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EduApp", "0037_alter_eduinst_address_alter_eduinst_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="eduinst",
            name="Completed_Courses",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="eduinst",
            name="Exam_Registrations",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="eduinst",
            name="Link",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="eduinst",
            name="Partnering_Institutes",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="eduinst",
            name="Student_Enrollment",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="eduinst",
            name="Successful_Certification",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
