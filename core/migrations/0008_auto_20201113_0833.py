# Generated by Django 3.0.8 on 2020-11-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201112_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='user',
            name='categ',
            field=models.CharField(default='0', max_length=2),
        ),
    ]