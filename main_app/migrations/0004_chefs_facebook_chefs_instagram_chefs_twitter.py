# Generated by Django 4.1.7 on 2023-04-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_chefs_events_gallery_reviews_special_whyus'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefs',
            name='facebook',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='chefs',
            name='instagram',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='chefs',
            name='twitter',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
