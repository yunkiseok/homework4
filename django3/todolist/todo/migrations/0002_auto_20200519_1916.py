# Generated by Django 3.0.6 on 2020-05-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='day',
        ),
        migrations.AlterField(
            model_name='post',
            name='due',
            field=models.DateTimeField(null=True),
        ),
    ]