# Generated by Django 2.0.4 on 2018-05-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
