# Generated by Django 2.1.7 on 2019-03-21 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0005_auto_20190320_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operatingsystem',
            old_name='product',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='language',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='other',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='sw_edition',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='target_hw',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='target_sw',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='update',
        ),
        migrations.RemoveField(
            model_name='operatingsystem',
            name='version',
        ),
        migrations.AddField(
            model_name='hardware',
            name='operating_system',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hardware.OperatingSystem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operatingsystem',
            name='description',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operatingsystem',
            name='note',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operatingsystem',
            name='operating_system',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hardware.NISTOperatingSystemOption'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operatingsystem',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.NISTVendorOption'),
        ),
    ]
