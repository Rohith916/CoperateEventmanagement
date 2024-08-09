# Generated by Django 5.0.1 on 2024-08-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trend', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=50)),
                ('organizer', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(max_length=255, upload_to='')),
                ('capacity', models.IntegerField()),
                ('small_description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('guest', models.CharField(max_length=255)),
                ('gmap', models.CharField(max_length=1000)),
                ('organization_details', models.TextField()),
                ('inclusions', models.TextField()),
                ('exclusions', models.TextField()),
            ],
        ),
    ]
