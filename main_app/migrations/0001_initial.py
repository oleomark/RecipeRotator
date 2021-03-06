# Generated by Django 3.2.3 on 2021-05-24 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cuisine', models.CharField(choices=[('NA', 'North American'), ('SA', 'South American'), ('LA', 'Latin American'), ('AS', 'Asian'), ('EU', 'European'), ('MD', 'Mediterranean'), ('AF', 'African')], default='NA', max_length=3)),
                ('instructions', models.TextField(max_length=500)),
                ('servingsize', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('ingredients', models.ManyToManyField(to='main_app.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_use', models.BooleanField(default=True)),
                ('date', models.DateField(verbose_name='Log Date')),
                ('name', models.CharField(max_length=50)),
                ('review', models.TextField(max_length=500)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.recipe')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
