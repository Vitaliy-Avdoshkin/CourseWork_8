# Generated by Django 5.1.3 on 2024-11-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="telegram-chat-id"
            ),
        ),
    ]
