# Generated by Django 3.2.5 on 2021-08-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_auto_20210809_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='product_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]