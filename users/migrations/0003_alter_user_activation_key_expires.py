# Generated by Django 3.2.6 on 2021-09-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210925_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
