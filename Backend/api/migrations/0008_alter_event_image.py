# Generated by Django 5.0.7 on 2024-08-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_event_trend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='eventmanagement/images'),
        ),
    ]