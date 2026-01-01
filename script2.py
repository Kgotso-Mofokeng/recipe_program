
#Recipe Program 2
import sys
import json


INGREDIENT_DB = "ingredients.json"
RECIPE_DB = "recipes.json"

# load databases to memory
def load_db(db):
	try:
		with open(db, "r") as f:
			return json.load(f)
	except:
		return {}

# save databases to disk
def save_db(db, data):
	with open(db, "w") as f:
		json.dump(data, f)


# Add ingredient to ingredient_db
def add_ingredient(ingredient_name):

	# Calculate price per unit (weight or volume)
	def price_per_unit():
		ingredient_price = float(input("Store price: "))
		ingredient_qty = float(input("Store quantity for price: "))
		unit = input("Unit (kg, g, l or ml): ").lower()

		# If units in kilograms
		if unit == "kg":
			price_per_kg = ingredient_price/ingredient_qty
			return price_per_kg

		# Unit in grams
		elif unit == "g":
			price_per_g = ingredient_price/ingredient_qty
			price_per_kg = price_per_g/1000
			return price_per_kg


		# Unit in l
		elif unit == "l":
			price_per_l = ingredient_price/ingredient_qty
			price_per_ml = price_per_l*1000
			return price_per_ml

		# Unit in ml
		elif unit == "ml":
			price_per_ml = ingredient_price/ingredient_qty
			return price_per_ml

	# Add ingredient to db
	ingredient_db = load_db(INGREDIENT_DB)
	ingredient_price_per_unit = price_per_unit()
	ingredient_db[ingredient_name.lower()] = ingredient_price_per_unit
	save_db(INGREDIENT_DB, ingredient_db)

	







# cli commands
if __name__ == "__main__":
	# argv[0] = script name
	# argv[1] = command
	# argv[2:] = arguments

	if len(sys.argv) < 3:
		print("Usage: python script.py add_ingredient <name>")
		sys.exit(1)

	command = sys.argv[1]

	if command == "add_ingredient":
		name = sys.argv[2]
		add_ingredient(name)

	# Add other if statements for other commands

	else:
		print(f"Unknown command: {command}")

ingredient_db = load_db(INGREDIENT_DB)
print(ingredient_db)


# Find a way to signify unit in ingredient database
# Continue to refactor current functions
# Find a way to add multiple ingredients using one command
