# Generated by Django 5.1.4 on 2024-12-11 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='description',
            new_name='contact',
        ),
    ]