# Generated by Django 4.1.4 on 2022-12-17 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_variation_options_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='orpsiyon adi ')),
            ],
        ),
        migrations.RemoveField(
            model_name='product_variations',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product_variations',
            name='option_id',
        ),
        migrations.AddField(
            model_name='product_variations',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.option', verbose_name=' Opsiyon Değeri '),
        ),
        migrations.AddField(
            model_name='product_variations',
            name='option_value',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.option_value', verbose_name='Opsiyon Değeri'),
        ),
    ]
