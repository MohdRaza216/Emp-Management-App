# Generated by Django 5.0.7 on 2024-08-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0004_alter_testimonial_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='img',
            field=models.ImageField(upload_to='testimonial/'),
        ),
    ]