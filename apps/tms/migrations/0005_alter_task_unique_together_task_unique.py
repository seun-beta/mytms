# Generated by Django 5.1 on 2024-09-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0004_task_campaign_alter_task_score'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('trainer', 'reviewer')},
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('trainer', 'reviewer'), name='unique'),
        ),
    ]
