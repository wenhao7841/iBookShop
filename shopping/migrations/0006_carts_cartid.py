# Generated by Django 3.0.7 on 2020-06-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20200609_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='CartID',
            field=models.CharField(default=0, max_length=20, unique=True),
        ),
    ]
