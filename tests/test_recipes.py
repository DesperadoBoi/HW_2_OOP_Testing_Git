import pytest

from src.recipes import Ingredient
from src.recipes import Recipe

def test_ingredient():
    ingredient = Ingredient("Мука", 600, "г")
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 600.0
    assert ingredient.unit == "г"

def test_ingredient_str():
    ingredient = Ingredient("Мука", 500, "г")

    assert str(ingredient) == "Мука: 500.0 г"

def test_ingredient_eq():
    first = Ingredient("Мука", 600, "г")
    second = Ingredient("Мука", 700, "г")
    third = Ingredient("Сахар", 500, "г")
    fourth = Ingredient("Мука", 500, "кг")

    assert first == second
    assert first != third
    assert first != fourth

def test_ingredient_bad_quantity():
    with pytest.raises(ValueError):
        Ingredient("Мука", 0, "г")


def test_recipe():
    recipe = Recipe("Блины")

    assert recipe.title == "Блины"
    assert len(recipe.ingredients) == 0


def test_recipe_add_ingredient():
    recipe = Recipe("Блины")
    ingredient = Ingredient("Мука", 600, "г")

    recipe.add_ingredient(ingredient)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0] == ingredient

def test_recipe_add_same_ingredient():
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 600, "г"))
    recipe.add_ingredient(Ingredient("Мука", 200, "г"))

    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 800.0


def test_recipe_scale():
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 600, "г"))
    recipe.add_ingredient(Ingredient("Молоко", 300, "мл"))

    scaled_recipe = recipe.scale(2)
    assert scaled_recipe.title == "Блины"
    assert len(scaled_recipe.ingredients) == 2
    assert scaled_recipe.ingredients[0].quantity == 1200.0
    assert scaled_recipe.ingredients[1].quantity == 600.0

def test_recipe_scale_not_change_original():
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))

    scaled_recipe = recipe.scale(2)

    assert recipe.ingredients[0].quantity == 500.0
    assert scaled_recipe.ingredients[0].quantity == 1000.0

def test_recipe_scale_bad_ratio():
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))

    with pytest.raises(ValueError):
        recipe.scale(0)

def test_recipe_len():
    recipe = Recipe("Блины")

    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Молоко", 300, "мл"))

    assert len(recipe) == 2