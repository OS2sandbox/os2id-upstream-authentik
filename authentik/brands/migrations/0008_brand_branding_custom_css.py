# Generated by Django 5.0.12 on 2025-02-22 01:51

from pathlib import Path
from django.db import migrations, models
from django.apps.registry import Apps

from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def migrate_custom_css(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    Brand = apps.get_model("authentik_brands", "brand")

    db_alias = schema_editor.connection.alias

    path = Path("/web/dist/custom.css")
    if not path.exists():
        return
    with path.read_text() as css:
        Brand.objects.using(db_alias).update(branding_custom_css=css)


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_brands", "0007_brand_default_application"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="branding_custom_css",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.RunPython(migrate_custom_css),
    ]
