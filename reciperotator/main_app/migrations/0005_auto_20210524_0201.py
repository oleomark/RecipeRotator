# Generated by Django 3.2.3 on 2021-05-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_recipelog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipelog',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='recipelog',
            name='date',
            field=models.DateField(verbose_name='Log Date'),
        ),
    ]
