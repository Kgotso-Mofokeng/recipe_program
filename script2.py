
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
	VALID_UNITS = {"kg", "g", "l", "ml"}

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


# Continue to refactor current functions
# Find a way to add multiple ingredients using one command
