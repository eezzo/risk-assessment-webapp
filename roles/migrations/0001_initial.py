# Generated by Django 2.1.7 on 2019-03-25 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('note', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'business_role',
            },
        ),
        migrations.CreateModel(
            name='SystemRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('note', models.TextField(max_length=255)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.System')),
            ],
            options={
                'db_table': 'system_role',
            },
        ),
        migrations.AddField(
            model_name='businessrole',
            name='system_role',
            field=models.ManyToManyField(blank=True, null=True, to='roles.SystemRole'),
        ),
    ]
