# Generated by Django 3.1.3 on 2020-11-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20201126_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
