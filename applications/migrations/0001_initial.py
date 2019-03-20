# Generated by Django 2.1.7 on 2019-03-16 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NISTApplicationOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=255)),
                ('release', models.CharField(blank=True, max_length=255, null=True)),
                ('update', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.CharField(blank=True, max_length=255, null=True)),
                ('sw_edition', models.CharField(blank=True, max_length=255, null=True)),
                ('target_sw', models.CharField(blank=True, max_length=255, null=True)),
                ('target_hw', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('other', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.NISTVendorOption')),
            ],
            options={
                'db_table': 'nist_application_option',
            },
        ),
    ]