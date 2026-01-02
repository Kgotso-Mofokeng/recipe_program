
#Recipe Program 2
import sys
import json


INGREDIENT_DB = "ingredients.json"
RECIPE_DB = "recipes.json"

# load database to memory
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


# Ingredient domain model
class Ingredient:
	VALID_UNITS = {"kg", "g", "l", "ml", "eggs"}

	def __init__(self, name, price, qty, unit):
		self.name = name
		self.price_per_unit, self.unit = self._normalize(price, qty, unit)

	def _normalize(self, price, qty, unit):
		if price <= 0:
			raise ValueError("Price must be positive")

		if qty <= 0:
			raise ValueError("Quantity must be positive")

		unit = unit.lower()

		if unit not in self.VALID_UNITS:
			raise ValueError(f"Unsupported unit: {unit}")

		# Weight
		if unit == "kg":
			return price / qty, "kg"

		if unit == "g":
			return (price / qty) * 1000, "kg"

		# Volume
		if unit == "l":
			return (price / qty) / 1000, "ml"

		if unit == "ml":
			return price / qty, "ml"

		# Eggs (edge case)
		if unit == "eggs":
			return price / qty

	# Serialization
	def to_dict(self):
		return {"price_per_unit": self.price_per_unit, "unit": self.unit}

# Recipe domain model
class Recipe:
	def __init__(self, name):
		self.name = name.lower()
		self.ingredients = [] # List of lists

	def add_ingredient(self, ingredient_name, qty, unit):
		if qty <= 0:
			return ValueError("Quantity must be positive")

		self.ingredients.append((ingredient_name.lower(), qty, unit.lower()))

	def normalize_qty(qty, unit, base_unit):
		if unit == base_unit:
			return qty

		# Weight
		if unit == "g" and base_unit == "kg":
			return qty / 1000

		# Volume
		if unit == "l" and base_unit == "ml":
			return qty * 1000

		raise ValueError(f"Incompatible units: {unit} -> {base_unit}")

	def compute_cost(self, ingredient_db):
		total_cost = 0.0

		for name, qty, unit in self.ingredients:
			if name not in ingredient_db:
				raise KeyError(f"Unknown ingredient: {name}")

			ingredient = ingredient_db[name]
			base_unit = ingredient["unit"]
			price_per_unit = ingredient["price_per_unit"]

			normalized_qty = normalize_qty(qty, unit, base_unit)
			total_cost += normalized_qty * price_per_unit
		return round(total_cost, 2)

	def to_dict(self):
		return {"ingredients": self.ingredients}

	@classmethod
	def from_dict(cls, name, data):
		recipe = cls(name)
		recipe.ingredients = data["ingredients"]
		return recipe

	def save_recipe(recipe):
		recipe_db = load_db(RECIPE_DB)
		recipe_db[recipe.name] = recipe.to_dict()
		save_db(RECIPE_DB, recipe_db)


def prompt_user():
	price = float(input("Store prices: "))
	qty = float(input("Store quantity for price: "))
	unit = input("Unit (kg, g, l or ml): ")
	return price, qty, unit

# Add ingredient to ingredient_db
def add_ingredient(name):

	ingredient_db = load_db(INGREDIENT_DB)

	try:
		price, qty, unit = prompt_user()
		ingredient = Ingredient(name, price, qty, unit)
		ingredient_db[ingredient.name] = ingredient.to_dict()
		save_db(INGREDIENT_DB, ingredient_db)
		print(f"Added ingredient: {ingredient.name}")

	except ValueError as e:
		print(f"Error: {e}")









# cli commands

# Command registry
COMMANDS = {}

def command(name):
	def decorator(func):
		COMMANDS[name] = func
		return func
	return decorator

def load_ingredients():
	return load_db(INGREDIENT_DB)

def load_recipes():
	return load_db(RECIPE_DB)

@command("add_recipe")
def add_recipe_cmd(args):
	if len(args) < 1:
		print("Usage: add_recipe <name>")
		return

	name = args[0]
	recipe = Recipe(name)

	recipe_db = load_recipes()
	recipe_db[recipe.name] = recipe.to_dict()
	save_db(RECIPE_DB, recipe_db)

	print(f"Recipe '{name}' created")

@command("add_recipe_ingredient")
def add_recipe_ingredient_cmd(args):
	if len(args) < 4:
		print("Usage: add_recipe_ingredient <recipe> <ingredient> <qty> <unit>")
		return

	recipe_name, ingredient_name, qty, unit = args

	recipe_db = load_recipes()

	if recipe_name not in recipe_db:
		print("Recipe not found")
		return

	recipe = Recipe.from_dict(recipe_name, recipe_db[recipe_name])

	try:
		recipe.add_ingredient(ingredient_name, float(qty), unit)

	except ValueError as e:
		print(e)
		return

	recipe_db[recipe.name] = recipe.to_dict()
	save_db(RECIPE_DB, recipe_db)

	print(f"Added {ingredient_name} to {recipe_name}")

@command("recipe_cost")
def recipe_cost_cmd(args):
	if len(args) < 1:
		print("Usage: recipe_cost <recipe>")
		return

	recipe_name = args[0]

	recipe_db = load_recipe()
	ingredient_db = load_ingredients()

	if recipe_name not in recipe_db:
		print("Recipe not found")
		return

	recipe = Recipe.from_dict(recipe_name, recipe_db[recipe_name])

	try:
		cost = recipe.compute_cost(ingredient_db)
		print(f"Total cost: R{cost}")
	except (ValueError, KeyError) as e:
		print(f"Error: {e}")















# Entry Point
if __name__ =="__main__":
	if len(sys.argv) < 2:
		print("Available commands:")
		for cmd in COMMANDS:
			print(f"  - {cmd}")
		sys.exit(1)

	cmd_name = sys.argv[1]
	args = sys.argv[2:]

	if cmd_name not in COMMANDS:
		print(f"Unknown command: {cmd_name}")
		sys.exit(1)

	COMMANDS[cmd_name](args)










ingredient_db = load_db(INGREDIENT_DB)
print(ingredient_db)
#recipe_db = load_db(RECIPE_DB)
#print(recipe_db)





# Add a command to modify ingredients in recipe database
# Eggs must be handled differently
