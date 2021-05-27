# Generated by Django 3.1.7 on 2021-05-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20210527_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipelog',
            name='rating',
            field=models.CharField(choices=[('One Star', 'ONE'), ('Two Star', 'TWO'), ('Three Star', 'THREE'), ('Four Star', 'FOUR'), ('Five Star', 'FIVE')], default='One Star', max_length=20),
        ),
    ]
