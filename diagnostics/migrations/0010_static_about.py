# Generated by Django 4.2.2 on 2024-09-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diagnostics", "0009_remove_static_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="static",
            name="about",
            field=models.TextField(blank=True, null=True, verbose_name="О нас"),
        ),
    ]
