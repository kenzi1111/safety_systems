# Generated by Django 4.2.6 on 2023-10-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="username",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
