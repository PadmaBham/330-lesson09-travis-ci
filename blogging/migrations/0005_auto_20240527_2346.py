# Generated by Django 3.1.5 on 2024-05-28 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_auto_20240527_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]
