# Generated by Django 2.0.6 on 2018-08-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingdescription',
            name='time',
            field=models.IntegerField(choices=[(30, '30 s'), (45, '45 s'), (60, '60 s'), (75, '75 s'), (90, '90 s'), (105, '105 s'), (120, '120 s')], default=30),
        ),
    ]