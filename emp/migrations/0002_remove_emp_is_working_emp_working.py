# Generated by Django 5.0.7 on 2024-08-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='is_working',
        ),
        migrations.AddField(
            model_name='emp',
            name='working',
            field=models.BooleanField(default=True),
        ),
    ]
