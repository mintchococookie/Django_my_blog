# Generated by Django 3.1.4 on 2020-12-18 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201217_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]
