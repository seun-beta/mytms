# Generated by Django 5.1 on 2024-09-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0002_rename_role_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='full_name',
            field=models.CharField(max_length=512),
        ),
    ]
