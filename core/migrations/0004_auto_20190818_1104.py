# Generated by Django 2.2.4 on 2019-08-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190818_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notfication',
            name='notification_type',
            field=models.CharField(blank=True, choices=[('Nolu cihaz açıldı', ' Nolu cihaz açıldı'), ('Nolu cihazı açmağa_cəhd_göstərildi', 'Nolu cihazı açmağa cəhd göstərildi')], max_length=50, null=True),
        ),
    ]
