# Generated by Django 2.2.4 on 2019-08-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190818_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='by_who',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
