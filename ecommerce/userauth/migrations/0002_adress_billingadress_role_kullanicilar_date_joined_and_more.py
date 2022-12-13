# Generated by Django 4.1.4 on 2022-12-11 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import userauth.models.adress
import userauth.models.profile


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Surname')),
                ('phone_number', models.IntegerField(unique=True, validators=[userauth.models.adress.validate_phone_number], verbose_name='Mobile Phone')),
                ('email_adress', models.EmailField(max_length=254, verbose_name='Email Adress')),
                ('is_active', models.BooleanField(verbose_name='Active User')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('town', models.CharField(max_length=30, verbose_name='Town')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('mailing_address', models.TextField(verbose_name='Mailing Address')),
            ],
        ),
        migrations.CreateModel(
            name='BillingAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Surname')),
                ('phone_number', models.IntegerField(unique=True, validators=[userauth.models.adress.validate_phone_number], verbose_name='Mobile Phone')),
                ('email_adress', models.EmailField(max_length=254, verbose_name='Email Adress')),
                ('is_active', models.BooleanField(verbose_name='Active User')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('town', models.CharField(max_length=30, verbose_name='Town')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('mailing_address', models.TextField(verbose_name='Mailing Address')),
                ('registered_addresses', models.ForeignKey(blank=True, help_text="you don't have to choose (optional)", null=True, on_delete=django.db.models.deletion.CASCADE, to='userauth.adress', verbose_name='Registered Addresses')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50, verbose_name='Role Name')),
                ('role_active', models.BooleanField(verbose_name='The role is active')),
            ],
        ),
        migrations.AddField(
            model_name='kullanicilar',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Surname')),
                ('phone_number', models.IntegerField(unique=True, validators=[userauth.models.profile.validate_phone_number], verbose_name='Mobile Phone')),
                ('date_of_birth', models.DateField(verbose_name='Date Of Birth')),
                ('validate_user', models.BooleanField(default=False, verbose_name='Verified User')),
                ('is_active', models.BooleanField(verbose_name='Active User')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.adress', verbose_name='The address of the user')),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.billingadress', verbose_name="User's billing address")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Users')),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.role', verbose_name='The Role Of The User')),
            ],
        ),
    ]