# Generated by Django 5.2.1 on 2025-05-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starGiftUnique', '0009_alter_userstargiftunique_star_gift_unique_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userstargiftunique',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='userstargiftunique',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
