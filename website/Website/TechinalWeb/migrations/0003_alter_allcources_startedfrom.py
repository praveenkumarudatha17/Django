# Generated by Django 4.0.6 on 2022-07-16 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechinalWeb', '0002_remove_details_il_remove_details_sp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcources',
            name='startedfrom',
            field=models.DateTimeField(verbose_name='Started From'),
        ),
    ]
