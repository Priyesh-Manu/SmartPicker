# Generated by Django 5.0.1 on 2024-01-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='message_date',
            field=models.DateField(auto_now=True),
        ),
    ]
