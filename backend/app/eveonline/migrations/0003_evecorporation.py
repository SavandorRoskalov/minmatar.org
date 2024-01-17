# Generated by Django 4.2.8 on 2023-12-11 03:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eveonline", "0002_alter_eveprimarytoken_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="EveCorporation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("corporation_id", models.IntegerField()),
                ("name", models.CharField(blank=True, max_length=255)),
                ("ticker", models.CharField(blank=True, max_length=255)),
                ("member_count", models.IntegerField(blank=True)),
                ("ceo_id", models.IntegerField(blank=True)),
                ("alliance_id", models.IntegerField(blank=True)),
                ("faction_id", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
