from numbers import Real


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', '{self.quantity}', '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title: str, ingredients=None):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []

    def add_ingredient(self, ingredient: Ingredient):
        for cur_ingredient in self.ingredients:
            if cur_ingredient == ingredient:
                cur_ingredient.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if (isinstance(ratio, int) or isinstance(ratio, float)) and ratio > 0:
            return True
        else:
            return False

    def scale(self, ratio: float):
        scaled = []
        for cur_ingredient in self.ingredients:
            scaled_ingr = Ingredient(cur_ingredient.name, cur_ingredient.quantity * ratio, cur_ingredient.unit)
            scaled.append(scaled_ingr)
        return Recipe(self.title, scaled)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ingredients_ = ", ".join(str(ingredient) for ingredient in self.ingredients)
        return f"Блюдо: {self.title}\nИнгредиенты: {ingredients_}"

# if __name__ == "__main__":
#     recipe = Recipe("Pancakes")
#
#     recipe.add_ingredient(Ingredient("Milk", 200.0, "ml"))
#     recipe.add_ingredient(Ingredient("Flour", 300.0, "g"))
#
#     print(recipe)