# Generated by Django 3.0.4 on 2020-03-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200305_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='observer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='record',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
