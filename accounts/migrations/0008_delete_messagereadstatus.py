# Generated by Django 4.2.6 on 2024-01-11 02:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_user_username_messagereadstatus"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MessageReadStatus",
        ),
    ]
