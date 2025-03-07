# Generated by Django 5.1.6 on 2025-03-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='dateCreated',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='isCompleted',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(default='CHANGETHIS', max_length=50),
            preserve_default=False,
        ),
    ]
