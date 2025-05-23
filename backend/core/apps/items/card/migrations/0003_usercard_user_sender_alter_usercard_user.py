# Generated by Django 5.2.1 on 2025-05-16 19:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_usercard_get_from_app'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usercard',
            name='user_sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usercard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards_received', to=settings.AUTH_USER_MODEL),
        ),
    ]
