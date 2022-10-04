# Generated by Django 4.1.1 on 2022-10-04 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 4, 16, 51, 13, 489498, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
