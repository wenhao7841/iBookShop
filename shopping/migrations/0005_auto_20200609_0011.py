# Generated by Django 3.0.7 on 2020-06-08 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20200609_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='MemberAdress',
            new_name='MemberAddress',
        ),
    ]
