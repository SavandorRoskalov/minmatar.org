# Generated by Django 4.2.8 on 2023-12-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "eveonline",
            "0012_alter_evecorporationapplication_discord_thread_id",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="EveCharacterSkillset",
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
                ("name", models.CharField(max_length=255)),
                ("skills", models.TextField(blank=True)),
            ],
        ),
    ]