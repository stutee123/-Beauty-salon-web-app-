# Generated by Django 3.1.1 on 2020-10-03 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0002_services_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='note',
        ),
    ]