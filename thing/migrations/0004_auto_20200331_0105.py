# Generated by Django 2.2.7 on 2020-03-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0003_auto_20200331_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
    ]
