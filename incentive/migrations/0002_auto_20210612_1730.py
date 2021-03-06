# Generated by Django 3.2.3 on 2021-06-12 12:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incentive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_detail',
            name='adhar_img',
            field=models.ImageField(upload_to='images/', verbose_name='Adhar_card Image'),
        ),
        migrations.AlterField(
            model_name='staff_detail',
            name='bank_img',
            field=models.ImageField(upload_to='images/', verbose_name='Bank Image'),
        ),
        migrations.AlterField(
            model_name='staff_detail',
            name='pan_img',
            field=models.ImageField(upload_to='images/', verbose_name='Pancard Image'),
        ),
        migrations.CreateModel(
            name='Nominee_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominee', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('relationship', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('village', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='Invalid', regex='^[0-9]{10}$')], verbose_name='Mobile Number')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pincode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incentive.address_detail', verbose_name='Pin Code')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incentive.staff_detail', verbose_name='Staff ID')),
            ],
            options={
                'verbose_name': 'Nominee Detail',
                'db_table': 'nominee_detail',
            },
        ),
    ]
