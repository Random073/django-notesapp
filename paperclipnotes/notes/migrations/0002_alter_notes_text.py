# Generated by Django 4.1 on 2023-11-07 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
