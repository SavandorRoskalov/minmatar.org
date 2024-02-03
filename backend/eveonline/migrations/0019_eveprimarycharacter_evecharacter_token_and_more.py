# Generated by Django 4.2.9 on 2024-02-03 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("esi", "0012_fix_token_type_choices"),
        ("eveonline", "0018_delete_evegroup"),
    ]

    operations = [
        migrations.CreateModel(
            name="EvePrimaryCharacter",
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
            ],
        ),
        migrations.AddField(
            model_name="evecharacter",
            name="token",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="esi.token",
            ),
        ),
        migrations.DeleteModel(
            name="EvePrimaryToken",
        ),
        migrations.AddField(
            model_name="eveprimarycharacter",
            name="character",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="eveonline.evecharacter",
            ),
        ),
    ]