# Generated by Django 3.2.5 on 2024-01-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0002_dweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dweet',
            name='cover',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
