# Generated by Django 4.0.3 on 2022-04-15 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_alter_bill_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
    ]
