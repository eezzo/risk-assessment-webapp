# Generated by Django 2.1.7 on 2019-04-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nistapplicationoption',
            name='product',
            field=models.CharField(max_length=255),
        ),
    ]
