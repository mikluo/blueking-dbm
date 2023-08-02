# Generated by Django 3.2.19 on 2023-08-01 08:34

from django.db import migrations, models

import backend.db_meta.enums.destroyed_status


class Migration(migrations.Migration):

    dependencies = [
        ("rollback", "0006_alter_tbtendisrollbacktasks_destroyed_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbtendisrollbacktasks",
            name="destroyed_status",
            field=models.IntegerField(
                choices=[(0, "Not destroyed"), (1, "Destroyed"), (2, "Destroying")],
                default=backend.db_meta.enums.destroyed_status.DestroyedStatus["NOT_DESTROYED"],
                verbose_name="销毁状态",
            ),
        ),
        migrations.AlterField(
            model_name="tbtendisrollbacktasks",
            name="related_rollback_bill_id",
            field=models.BigIntegerField(verbose_name="单据号，关联单据"),
        ),
    ]
