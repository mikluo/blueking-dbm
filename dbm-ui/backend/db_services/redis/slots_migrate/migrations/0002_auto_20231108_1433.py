# Generated by Django 3.2.19 on 2023-11-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slots_migrate", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbtendisslotsmigraterecord",
            name="current_group_num",
            field=models.IntegerField(default=0, verbose_name="扩缩容前的主机数量"),
        ),
        migrations.AlterField(
            model_name="tbtendisslotsmigraterecord",
            name="target_group_num",
            field=models.IntegerField(default=0, verbose_name="扩缩容后的主机数量"),
        ),
    ]
