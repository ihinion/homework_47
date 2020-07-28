# Generated by Django 2.2 on 2020-07-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('status', models.TextField(default='new', max_length=15, verbose_name='Status')),
                ('finished', models.DateField(blank=True, default='', max_length=10, null=True, verbose_name='Finished')),
            ],
        ),
    ]
