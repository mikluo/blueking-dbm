# Generated by Django 3.2.19 on 2023-11-11 08:16

from django.db import migrations, models

import backend.db_meta.enums.destroyed_status


class Migration(migrations.Migration):

    dependencies = [
        ("slots_migrate", "0003_auto_20231108_1441"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbtendisslotsmigraterecord",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Not started"), (1, "Executing"), (2, "Completed"), (-1, "Erroroccurred")],
                default=backend.db_meta.enums.destroyed_status.MigrateStatus["NOT_STARTED"],
                verbose_name="状态",
            ),
        ),
    ]
