# Generated by Django 5.1.2 on 2024-10-18 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_generos'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='fk_generos',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.generos'),
        ),
    ]
