#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = 0
    first_pass = True

    for rec_item in recipe:
        if rec_item in ingredients:
            # item exists in ingredients
            possible_batches = ingredients[rec_item] // recipe[rec_item]
            if first_pass:
                batches = possible_batches
                first_pass = False
            else:
                if possible_batches < batches:
                    batches = possible_batches
        else:
            # Item does not exist in our ingredients
            batches = 0
            break

    return batches


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

