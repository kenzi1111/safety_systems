# Generated by Django 4.2.6 on 2024-01-17 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0007_messagereadstatus"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessageRecipient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("read_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="message",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="chat.room",
            ),
        ),
        migrations.DeleteModel(
            name="MessageReadStatus",
        ),
        migrations.AddField(
            model_name="messagerecipient",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="chat.message"
            ),
        ),
        migrations.AddField(
            model_name="messagerecipient",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name="messagerecipient",
            unique_together={("message", "recipient")},
        ),
    ]
