# Generated by Django 3.1.5 on 2024-05-28 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0003_auto_20240527_2318"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="category",
            new_name="categories",
        ),
    ]
