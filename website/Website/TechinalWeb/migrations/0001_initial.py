# Generated by Django 4.0.6 on 2022-07-15 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllCources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courcename', models.CharField(max_length=100)),
                ('instructorname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp', models.CharField(max_length=300)),
                ('il', models.CharField(max_length=300)),
                ('cources', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechinalWeb.allcources')),
            ],
        ),
    ]