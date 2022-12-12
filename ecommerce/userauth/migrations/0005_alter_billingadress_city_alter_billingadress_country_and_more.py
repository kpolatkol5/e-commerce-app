# Generated by Django 4.1.4 on 2022-12-11 15:41

from django.db import migrations, models
import userauth.models.adress


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_alter_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingadress',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='email_adress',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Adress'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='is_active',
            field=models.BooleanField(blank=True, null=True, verbose_name='Active User'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='last_name',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='mailing_address',
            field=models.TextField(blank=True, null=True, verbose_name='Mailing Address'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[userauth.models.adress.validate_phone_number], verbose_name='Mobile Phone'),
        ),
        migrations.AlterField(
            model_name='billingadress',
            name='town',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Town'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active User'),
        ),
    ]
