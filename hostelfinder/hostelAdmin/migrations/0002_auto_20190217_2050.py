# Generated by Django 2.1.5 on 2019-02-17 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostelAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_fee', models.CharField(max_length=250)),
                ('refundable_fee', models.CharField(max_length=250)),
                ('security_fee', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=250)),
                ('hostel_type', models.CharField(choices=[('G', 'Girls Hostel'), ('B', 'Boys Hostel')], max_length=20)),
                ('hostel_phone', models.CharField(max_length=100)),
                ('hostel_mobile', models.CharField(max_length=100)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostelAdmin.Geography')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.CharField(max_length=250)),
                ('image1', models.CharField(default='n/a', max_length=250)),
                ('image2', models.CharField(default='n/a', max_length=250)),
                ('image3', models.CharField(default='n/a', max_length=250)),
                ('image4', models.CharField(default='n/a', max_length=250)),
                ('image5', models.CharField(default='n/a', max_length=250)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelAdmin.Hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250)),
                ('street', models.CharField(default='Kathmandu', max_length=250)),
                ('province', models.IntegerField(default=3)),
                ('zip', models.CharField(max_length=250)),
                ('country', models.CharField(default='Nepal', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seater_type', models.IntegerField(default=1)),
                ('quantity', models.IntegerField(default=1)),
                ('room_price', models.CharField(max_length=250)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelAdmin.Hostel')),
            ],
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='hostel',
        ),
        migrations.DeleteModel(
            name='Hostels',
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
        migrations.AddField(
            model_name='fee',
            name='hostel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelAdmin.Hostel'),
        ),
    ]
