# Generated by Django 3.1.7 on 2021-05-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20210527_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipelog',
            name='rating',
            field=models.CharField(choices=[('', '★'), ('', '★★'), ('', '★★★'), ('', '★★★★'), ('', '★★★★★')], default='', max_length=20),
        ),
    ]
