# Generated by Django 2.0.4 on 2018-04-08 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spacyal', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='case',
            unique_together={('hash', 'suggestion')},
        ),
    ]
