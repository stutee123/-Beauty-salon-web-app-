# Generated by Django 3.1.1 on 2020-10-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0004_fullservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacialMassage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facialMassage', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('hours', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HairCare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hairCare', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('hours', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HairStyles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hairStyles', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('hours', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MakeUpServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('makeUpServices', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('hours', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manicure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manicure', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('hours', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NailArts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nailArts', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('hours', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedicure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedicure', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('hours', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FullServices',
        ),
        migrations.RemoveField(
            model_name='services',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='services',
            name='price',
        ),
    ]