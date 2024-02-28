# Generated by Django 4.2.5 on 2024-02-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loanamout",
            name="martialStatus",
            field=models.CharField(
                choices=[
                    ("Married", "Married"),
                    ("UnMarried", "UnMarried"),
                    ("Single", "Single"),
                ],
                default="",
                max_length=10,
            ),
        ),
    ]
