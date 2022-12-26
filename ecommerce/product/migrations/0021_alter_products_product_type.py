# Generated by Django 4.1.4 on 2022-12-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_option_value_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_type',
            field=models.CharField(choices=[('P', 'Fiziksel ürün'), ('D', 'Dijital Ürün')], max_length=20, verbose_name='Ürün Tipi'),
        ),
    ]
