# Generated by Django 4.1.4 on 2022-12-17 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_product_variation_options_product_variations_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_variation_options',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.products', verbose_name='Ürün'),
            preserve_default=False,
        ),
    ]