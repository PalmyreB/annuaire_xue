import json

from django.db import migrations
from django.utils.text import slugify

from entrees import models


def create_fields_of_competence(apps, schema_editor):
    """Populate database with fields of competence from file"""
    FieldOfCompetence = models.FieldOfCompetence
    with open(
        "./entrees/migrations/migration_files/fields_of_competence.json",
        "r",
        encoding="utf8",
    ) as field_file:
        data = field_file.read()
    field_list = json.loads(data)
    for field_name in field_list:
        field = {
            "name": field_name,
            "slug": slugify(field_name).replace("&", "-et-"),
        }
        FieldOfCompetence.objects.create(**field)


def delete_fields_of_competence(apps, schema_editor):
    """Reverse operation: delete all fields of competence"""
    models.FieldOfCompetence.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("entrees", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_fields_of_competence, delete_fields_of_competence),
    ]
