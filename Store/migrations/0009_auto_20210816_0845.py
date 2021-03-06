# Generated by Django 3.2.5 on 2021-08-16 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='banner',
            name='large',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='Store.product'),
        ),
    ]
