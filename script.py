# Simple Recipe Cost Calculator

print("RECIPE COST CALCULATOR")
print("----------------------")

# Data Structures , recipes should be empty, but is populated for test purposes
recipes = {
    "Green Pasta":{
        "Spaghetti": 30,
        "Red cabbage": 35,
        "Regular cabbage": 25,
        "Onions": 20,
        "Ground beef (mince)": 60,
        "Carrots": 25,
        "Potatoes": 15,
        "Salt": 35,
        "Barbeque spice": 50,
        "Sunflower oil": 25
    },

    "Mince Macaroni":{
        "Macaroni": 67,
        "Beef mincemeat (lean)": 35,
        "Tomato paste": 35,
        "Braai sauce": 37,
        "Onion": 13,
        "Green pepper": 30,
        "Garlic (crushed)": 56,
        "Mild Rajah": 76,
        "Beef spice": 45,
        "Beef stock cubes": 2,
        "Sunflower oil": 34
    }
}



while True:
    recipe_name = input("\nEnter recipe name (or 'exit'): ")
    if recipe_name.lower() == "exit":
        break

    recipes[recipe_name] = {}

    while True:
        ingredient = input("Enter ingredient name (or type 'done'): ")
        if ingredient.lower() == "done":
            break

        price = float(input("Enter price of {ingredient}: ".format(ingredient=ingredient)))
        recipes[recipe_name][ingredient] = price
        



def compare_recipes(recipes_dict):
    for recipe, ingredients in recipes.items():
        total = sum(ingredients.values())
        print(recipe, "-> R", round(total, 2))

