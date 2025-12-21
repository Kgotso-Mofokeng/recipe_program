# Simple Recipe Cost Calculator


print("RECIPE COST CALCULATOR")
print("----------------------")

recipe_name = input("Enter recipe name: ")
total_cost = 0.0

while True:
    ingredient = input("Enter ingredient name (or type 'done'): ")
    if ingredient.lower() == "done":
        break

    price = float(input("Enter price of {ingredient}: ".format(ingredient=ingredient)))
    total_cost = total_cost + price

print("\n---------------------")
print("Recipe:", recipe_name)
print("Total cost: R", round(total_cost, 2))
print("-----------------------")