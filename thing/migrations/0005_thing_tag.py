# Generated by Django 2.2.7 on 2020-03-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0004_auto_20200331_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='tag',
            field=models.CharField(blank=True, max_length=100, verbose_name='Тег'),
        ),
    ]
