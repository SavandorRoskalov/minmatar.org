# Generated by Django 4.2.8 on 2023-12-26 22:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("eveonline", "0017_remove_evealliance_member_count"),
    ]

    operations = [
        migrations.DeleteModel(
            name="EveGroup",
        ),
    ]