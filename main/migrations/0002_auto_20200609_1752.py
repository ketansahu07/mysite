# Generated by Django 3.0.6 on 2020-06-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
