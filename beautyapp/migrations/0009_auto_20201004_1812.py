# Generated by Django 3.1.1 on 2020-10-04 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0008_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FacialMassage',
            new_name='FacialTreatment',
        ),
        migrations.AlterModelOptions(
            name='makeupservices',
            options={'verbose_name_plural': 'Make Up Services'},
        ),
        migrations.AlterModelOptions(
            name='nailarts',
            options={'verbose_name_plural': 'Nail Arts'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.RenameField(
            model_name='facialtreatment',
            old_name='facialMassage',
            new_name='facialTreatment',
        ),
    ]
