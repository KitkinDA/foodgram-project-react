from django.db import migrations


INITIAL_TAGS = [
    {"name": "Ужин", "color": "purple", "slug": "dinner"},
    {"name": "Завтрак", "color": "orange", "slug": "breakfast"},
    {"name": "Обед", "color": "green", "slug": "lunch"}
    # {"name": "Перекус", "color": "yellow", "slug": "snack"},
]


def add_tags(apps, schema_editor):
    Tag = apps.get_model("recipes", "Tag")
    for tag in INITIAL_TAGS:
        new_tag = Tag(name=tag["name"], color=tag["color"], slug=tag["slug"])
        new_tag.save()


def remove_tags(apps, schema_editor):
    Tag = apps.get_model("recipes", "Tag")
    for tag in INITIAL_TAGS:
        Tag.objects.get(slug=tag["slug"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [migrations.RunPython(add_tags, remove_tags)]
