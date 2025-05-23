# Generated by Django 5.2.1 on 2025-05-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starGiftUnique', '0014_alter_userstargiftunique_lottie_animation_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstargiftunique',
            name='backdrop',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userstargiftunique',
            name='num',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userstargiftunique',
            name='pattern',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userstargiftunique',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
