# Generated by Django 5.2.1 on 2025-05-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_referals'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_popularity',
            field=models.FloatField(db_index=True, default=0),
        ),
    ]
