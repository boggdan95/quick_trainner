# Generated by Django 2.0.6 on 2018-07-05 01:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_presettrainingsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('results', django.contrib.postgres.fields.jsonb.JSONField()),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.TrainingDescription')),
            ],
        ),
    ]
