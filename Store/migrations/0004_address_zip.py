# Generated by Django 3.2.5 on 2021-08-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]