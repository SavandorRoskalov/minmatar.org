# Generated by Django 4.2.9 on 2024-02-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discord", "0003_alter_discordrole_role_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discorduser",
            name="avatar",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
