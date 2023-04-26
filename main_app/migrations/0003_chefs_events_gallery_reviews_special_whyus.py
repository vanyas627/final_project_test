# Generated by Django 4.1.7 on 2023-04-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_dishes_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('photo', models.ImageField(upload_to='chefs')),
            ],
            options={
                'verbose_name_plural': 'Шефи',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.PositiveSmallIntegerField()),
                ('desc', models.TextField(max_length=1000)),
                ('photo', models.ImageField(upload_to='events')),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Події',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery')),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Галерея',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='reviews')),
                ('desc', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Відгуки',
            },
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('position', models.PositiveSmallIntegerField()),
                ('desk', models.TextField(max_length=1000)),
                ('ingredients', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(upload_to='dishes')),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Спеціальні страви',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Whyus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=1000)),
                ('position', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0)),
            ],
            options={
                'verbose_name_plural': 'Why choose our restaurant',
                'ordering': ('position',),
            },
        ),
    ]