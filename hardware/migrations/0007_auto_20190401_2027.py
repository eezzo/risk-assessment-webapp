# Generated by Django 2.1.7 on 2019-04-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0006_auto_20190321_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nistvendoroption',
            name='name',
            field=models.CharField(max_length=355),
        ),
    ]