# Generated by Django 3.0.7 on 2020-09-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountaboddiesapi', '0003_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='population',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='group',
            name='size',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]
