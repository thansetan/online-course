# Generated by Django 4.2.1 on 2023-06-07 13:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("onlinecourse", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="question",
            new_name="question_text",
        ),
    ]
