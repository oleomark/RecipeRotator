# Generated by Django 3.1.7 on 2021-05-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20210526_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipelog',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5),
        ),
    ]
