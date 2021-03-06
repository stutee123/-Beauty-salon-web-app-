# Generated by Django 3.1.1 on 2020-10-09 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0012_auto_20201009_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingFacialTreatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('facialtreatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.facialtreatment')),
            ],
        ),
        migrations.CreateModel(
            name='BookingHaircare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('haircare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.haircare')),
            ],
        ),
        migrations.CreateModel(
            name='BookingHairStyles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('hairstyles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.hairstyles')),
            ],
        ),
        migrations.CreateModel(
            name='BookingMakeUpServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('makeupservices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.makeupservices')),
            ],
        ),
        migrations.CreateModel(
            name='BookingManicure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('manicure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.manicure')),
            ],
        ),
        migrations.CreateModel(
            name='BookingNailArts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('nailarts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.nailarts')),
            ],
        ),
        migrations.CreateModel(
            name='BookingPedicure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('pedicure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.pedicure')),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
