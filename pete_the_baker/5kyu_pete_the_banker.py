"""recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
"""
"""for ingredient_r,amount_r in recipe.items():
    if ingredient_r not in available:
        print(f"Missing {ingredient_r}")

for ingredient_a, amount_a in available.items():
    if amount_r <= 

"""


def cakes(recipe, available):
    recipe = recipe
    available = available
    rations = []
    for ingredient_r, amount_r in recipe.items():
        if ingredient_r not in available:
            print(f"Missing {ingredient_r}")
            return 0
        elif available[ingredient_r] < amount_r:
            print(f"Not enough {ingredient_r}")
            return 0
        else:
            a = available[ingredient_r] / recipe[ingredient_r]
            rations.append(a)
    return int(min(rations))

cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})