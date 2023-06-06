import json
import os

from django.db import migrations, transaction


def add_ingredients(apps, schema_editor):
    Ingredient = apps.get_model("recipes", "Ingredient")
    print(os.getcwd())
    with open("ingredients.json", encoding="utf-8") as file:
        ingredients = json.load(file)
        for ingredient in ingredients:
            with transaction.atomic():
                Ingredient.objects.create(
                    name=ingredient["name"],
                    measurement_unit=ingredient["measurement_unit"],
                )


def remove_ingredients(apps, schema_editor):
    Ingredient = apps.get_model("recipes", "Ingredient")
    Ingredient.objects.all().delete()
    with open("ingredients.json", encoding="utf-8") as file:
        ingredients = json.load(file)
        for ingredient in ingredients:
            Ingredient.objects.get(name=ingredient["name"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "add_tags"),
    ]

    operations = [migrations.RunPython(add_ingredients, remove_ingredients)]
