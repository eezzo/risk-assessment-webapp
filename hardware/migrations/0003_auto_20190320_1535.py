# Generated by Django 2.1.7 on 2019-03-20 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0002_auto_20190318_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hardware',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='language',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='other',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='product',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='sw_edition',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='target_hw',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='target_sw',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='update',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='version',
        ),
        migrations.AddField(
            model_name='hardware',
            name='hardware',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hardware.NISTHardwareOption'),
            preserve_default=False,
        ),
    ]
