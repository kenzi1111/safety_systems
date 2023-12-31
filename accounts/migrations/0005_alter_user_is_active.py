# Generated by Django 4.2.6 on 2023-12-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_userprofile_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active.Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
