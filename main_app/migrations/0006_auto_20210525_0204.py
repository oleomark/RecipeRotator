# Generated by Django 3.1.7 on 2021-05-25 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210525_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='name',
            new_name='ingredient_name',
        ),
    ]
