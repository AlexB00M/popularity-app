# Generated by Django 5.2.1 on 2025-05-19 23:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starGiftUnique', '0006_alter_userstargiftunique_star_gift_unique_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstargiftunique',
            name='star_gift_unique',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='received_by_user', to='starGiftUnique.stargiftunique'),
        ),
        migrations.AlterField(
            model_name='userstargiftunique',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='received_star_gift_unique', to=settings.AUTH_USER_MODEL),
        ),
    ]
