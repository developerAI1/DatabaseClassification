# Generated by Django 4.1.7 on 2023-07-13 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_databasename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionandanswr',
            name='user_id',
        ),
    ]