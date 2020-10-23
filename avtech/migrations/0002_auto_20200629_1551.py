# Generated by Django 3.0.7 on 2020-06-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtech', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='think',
            name='idea',
        ),
        migrations.AddField(
            model_name='think',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='think',
            name='author',
            field=models.CharField(max_length=500),
        ),
    ]
