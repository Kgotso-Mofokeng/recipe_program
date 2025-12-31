# Recipe Program

## Recipe Class
### Properties
1. recipe_name
2. ingredients_list

## Ingredient Class
### Properties
1. ingredient_name
2. get_price_per_unit method

## Recipe Database 
```python
recipe_database = { 
			"recipe_name1" : ["ingredient_name1", "ingredient_name2", . . .],
			"recipe_name2" : ["ingredient_name2", "ingredient_name2", . . .]
			}

ingredient_database = {
			"ingredient_name1" : "ingredient_name1.get_price_per_unit",
			"ingredient_name2" : "ingredient_name2.get_price_per_unit"
			}
# Export databases as JSON

```

## add_ingredient function
Adds ingredient_name and price per unit to ingredient database

## list_ingredient_price
Outputs ingredient -> price based on quantity
two arguments: ingredient_name and quantity
create a function to calculate price based on quantity
it can take multiple arguments and list them accordinly

## add_recipe function
add_recipe() adds recipe_name and ingredient_name to recipe_database

## list_recipe_price function
Outputs recipe_naame -> total price
one arg recipe_name
it can take multiple inputs and list recipe_names and total prices accordinly


## list_recipe_price_all function
1. Lists all recipe_names and their total ingredient_prices
2. Loop through recipe_database and sum ingredient_database[ingredient_name]


