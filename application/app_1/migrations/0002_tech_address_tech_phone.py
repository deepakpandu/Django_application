# Generated by Django 4.2.3 on 2023-07-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tech',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tech',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
