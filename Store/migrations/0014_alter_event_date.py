# Generated by Django 3.2.5 on 2021-08-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
