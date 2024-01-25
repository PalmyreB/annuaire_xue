import json

from django.db import migrations
from django.utils.text import slugify

from contacts import models


def create_fields_of_competence(apps, schema_editor):
    """Populate database with fields of competence from file"""
    FieldOfCompetence = models.FieldOfCompetence
    with open(
        "./contacts/migrations/migration_files/fields_of_competence.json",
        "r",
        encoding="utf8",
    ) as field_file:
        data = field_file.read()
    field_list = json.loads(data)
    for field_item in field_list:
        field_item["slug"] = (
            slugify(field_item["name"]).replace("&", "-et-").replace("/", "-")
        )
        FieldOfCompetence.objects.create(**field_item)


def delete_fields_of_competence(apps, schema_editor):
    """Reverse operation: delete all fields of competence"""
    models.FieldOfCompetence.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_fields_of_competence, delete_fields_of_competence),
    ]
