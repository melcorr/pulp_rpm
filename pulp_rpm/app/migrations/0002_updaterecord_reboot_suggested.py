# Generated by Django 2.2.7 on 2019-11-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='updaterecord',
            name='reboot_suggested',
            field=models.BooleanField(default=False),
        ),
    ]
