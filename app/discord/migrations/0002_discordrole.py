# Generated by Django 4.2.8 on 2023-12-18 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("discord", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscordRole",
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
                ("role_id", models.BigIntegerField()),
                ("name", models.CharField(max_length=100)),
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="discord_group",
                        to="auth.group",
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="groups", to="discord.discorduser"
                    ),
                ),
            ],
        ),
    ]