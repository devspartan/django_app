# Generated by Django 3.1.1 on 2020-09-08 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_test',
            new_name='question_text',
        ),
    ]
