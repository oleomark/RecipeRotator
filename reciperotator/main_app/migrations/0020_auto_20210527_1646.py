# Generated by Django 3.1.7 on 2021-05-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20210527_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipelog',
            name='recipe_use',
            field=models.BooleanField(default=False),
        ),
    ]
