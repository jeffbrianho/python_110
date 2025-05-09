# Pete is baking cakes and needs help calculating how many he can make with his recipes and available ingredients.
# Write a function cakes() that takes two dictionaries: the recipe and the available ingredients. 
# Return the maximum number of cakes Pete can bake.

# Rules:
# - Ingredients not present in the objects can be considered as 0.

"""
compare the dictionaries:
for recipe dict[flour] vs ingredients divide the whole number of each value
use a list to store num - min num is answer. 

"""
def cakes(recipe, ingredients):
    try:
        return min([ingredients[item] // amount if item in ingredients
                                                else 0 
                                                for item, amount in recipe.items()])
    except ValueError:
        return 0
            
            

# must return 2
print(cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2)

# # must return 11
print(cakes({"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 1700, "flour": 20000,
"milk": 20000, "oil": 30000, "cream": 5000}) == 11)

# must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000,
"milk": 2000}) == 0)

# must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000,
"milk": 2000, "apples": 15, "oil": 20}) == 0)

# must return 0
print(cakes({"eggs": 4, "flour": 400},{}) == 0)

# must return 1
print(cakes({"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1},{"sugar": 1, "eggs": 1, "flour": 3,
"cream": 1, "oil": 1, "milk": 1}) == 1)