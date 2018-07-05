# Generated by Django 2.0.6 on 2018-07-05 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_trainingdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresetTrainingSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.TrainingType')),
            ],
        ),
    ]
