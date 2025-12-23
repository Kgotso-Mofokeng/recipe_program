# Simple Recipe Cost Calculator

print("RECIPE COST CALCULATOR")
print("----------------------")

# Data Structures , recipes should be empty, but is populated for test purposes
# Recipe, ingredients and quantity
recipes = {
    "Green Pasta":{
        "Spaghetti": 0.2,
        "Red cabbage": 0.2,
        "Regular cabbage": 0.2,
        "Onion": 0.05,
        "Ground beef (mince)": 0.1,
        "Carrots": 0.2,
        "Potatoes": 0.1,
        "Salt": 0.005, 
        "Barbeque spice": 0.005,
        "Sunflower oil": 0.025
    },

    "Mince Macaroni":{
        "Macaroni": 0.32,
        "Beef mincemeat (lean)": 0.3,
        "Tomato paste": 0.03,
        "Braai sauce": 0.025,
        "Onion": 0.065,
        "Green pepper": 0.1,
        "Garlic (crushed)": 0.003,
        "Mild Rajah": 0.005,
        "Beef spice": 0.005,
        "Beef stock cubes": 0.002,
        "Sunflower oil": 0.06
    }
}

# Ingredients Database populated with test data
# Ingredient and price per kg
ingredient_prices = {
    "Spaghetti": 26.99,
    "Red cabbage": 24.99,
    "Regular cabbage": 24.99,
    "Onion": 12.99,
    "Ground beef (mince)": 119.99,
    "Beef mincemeat (lean)": 119.99,
    "Carrots": 13.99,
    "Potatoes": 12.99,
    "Salt": 150, 
    "Barbeque spice": 300,
    "Sunflower oil": 37.99,
    "Macaroni": 25.98,
    "Tomato paste": 60,
    "Braai sauce": 100,
    "Green pepper": 35,
    "Garlic (crushed)": 80,
    "Mild Rajah": 300,
    "Beef spice": 300,
    "Beef stock cubes": 2500,
}




# Add ingredients and prices
while True:
    name = input("\nEnter ingredient name (or 'done'): ")
    if name.lower() == "done":
        break

    price = float(input(f"Price per kg for {name}: "))
    ingredient_prices[name] = price



# Add recipes
while True:
    recipe_name = input("\nEnter recipe name (or 'exit'): ")
    if recipe_name.lower() == "exit":
        break

    recipes[recipe_name] = {}

    # recipe:ingredients key:value
    while True:
        ingredient = input("Ingredient name (or 'done'): ")
        if ingredient.lower() == "done":
            break
        
        if ingredient not in ingredient_prices:
            print(f"{ingredient} not in price database!")

            # Add function that adds ingredient to database
            continue

        quantity = float(input("Quantity in kg: "))
        recipes[recipe_name][ingredient] = quantity





def recipe_cost(recipes):
    print("\nRECIPE COSTS")
    print("---------------")

    for recipe, ingredients in recipes.items():
        total_cost = 0

        for ingredient, qty in ingredients.items():
            price_per_kg = ingredient_prices[ingredient]
            total_cost = total_cost + price_per_kg * qty
    
        print(recipe, "-> R", round(total_cost, 2))



# NOTES:
# Add a quantity for milliliters

# Current state of program:
# - Add to ingredients and recipes databases
# - Print and comapre total prices of recipes