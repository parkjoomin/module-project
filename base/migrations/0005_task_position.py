# Generated by Django 5.0 on 2023-12-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_task_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
