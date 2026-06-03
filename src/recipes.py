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


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        scaled = recipe.scale(portions)
        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title:str):
        new_items = []

        for item in self._items:
            item_ingredient = item[0]
            item_title = item[1]
            if item_title != title:
                new_items.append((item_ingredient, item_title))

        self._items = new_items

    def get_list(self):
        result = {}

        for item in self._items:
            ingredient = item[0]
            key = (ingredient.name, ingredient.unit)
            if key in result:
                result[key] += ingredient.quantity
            else:
                result[key] = ingredient.quantity

        ingredients = []

        for key in result:
            name = key[0]
            unit = key[1]
            quant = result[key]
            ingredients.append(Ingredient(name, unit, quant))
        ingredients.sort(key=lambda x : x.name)

        return ingredients

    def __add__(self, other: "ShoppingList"):
        new_list = ShoppingList
        for item in self._items:
            new_list.append(item)
        for item in other._items:
            new_list.append(item)

        return new_list


