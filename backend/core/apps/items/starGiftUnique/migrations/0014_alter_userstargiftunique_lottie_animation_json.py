# Generated by Django 5.2.1 on 2025-05-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starGiftUnique', '0013_alter_userstargiftunique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstargiftunique',
            name='lottie_animation_json',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
