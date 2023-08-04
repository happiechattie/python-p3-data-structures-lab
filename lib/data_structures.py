spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = [item["name"] for item in spicy_foods if True]
    return new_list

def get_spiciest_foods(spicy_foods):
    new_list = [item for item in spicy_foods if item['heat_level'] > 5]
    return new_list

def print_spicy_foods(spicy_foods):
   for i in spicy_foods:
        print(f'{i["name"]} ({i["cuisine"]}) | Heat Level: {"🌶" * i["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"] == cuisine:
            return item

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat_levels = [item["heat_level"] for item in spicy_foods if True]
    return sum(heat_levels) / len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


print_spicy_foods(spicy_foods)