# Generated by Django 4.1.1 on 2022-10-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_level',
            field=models.CharField(choices=[('1', 'Fundamental Awareness'), ('2', 'Novice'), ('3', 'Intermediate'), ('4', 'Advanced'), ('5', 'Expert')], default='1', max_length=1),
        ),
    ]
