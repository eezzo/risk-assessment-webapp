# Generated by Django 2.1.7 on 2019-03-21 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0006_auto_20190321_1131'),
        ('applications', '0002_remove_nistapplicationoption_release'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('note', models.TextField(max_length=255)),
                ('cpe_string', models.CharField(blank=True, max_length=255, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.NISTApplicationOption')),
                ('hardware', models.ManyToManyField(to='hardware.Hardware')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.NISTVendorOption')),
            ],
            options={
                'db_table': 'application',
            },
        ),
    ]
