# Generated by Django 4.1.4 on 2022-12-17 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_variations_option_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_variations',
            name='option',
        ),
        migrations.AddField(
            model_name='option_value',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.option', verbose_name='Option'),
        ),
    ]
