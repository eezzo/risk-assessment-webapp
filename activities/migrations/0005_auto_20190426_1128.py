# Generated by Django 2.1.7 on 2019-04-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('activities', '0004_auto_20190426_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemactivity',
            name='system_role',
        ),
        migrations.AddField(
            model_name='systemactivity',
            name='system_role',
            field=models.ManyToManyField(to='roles.SystemRole'),
        ),
    ]