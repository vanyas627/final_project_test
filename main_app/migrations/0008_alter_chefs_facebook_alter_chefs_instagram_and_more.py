# Generated by Django 4.1.7 on 2023-04-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_events_caus_events_desc_caus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefs',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='twitter',
            field=models.URLField(blank=True),
        ),
    ]
