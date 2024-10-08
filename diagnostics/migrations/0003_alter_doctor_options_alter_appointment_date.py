# Generated by Django 5.1 on 2024-09-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diagnostics", "0002_rename_results_result_rename_services_service"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="doctor",
            options={
                "ordering": ["name"],
                "verbose_name": "Врач",
                "verbose_name_plural": "Врачи",
            },
        ),
        migrations.AlterField(
            model_name="appointment",
            name="date",
            field=models.DateField(auto_now_add=True, verbose_name="Дата записи"),
        ),
    ]
