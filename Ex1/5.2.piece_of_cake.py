def get_recipe_price(prices={}, optionals=[], **ingredients):
    """
    Calculate the price that have to pay for buy the products for the cake
    :param prices: Dictionary of products needed for the recipe,
                   the keys are the products and the values are the price per 100 gr.
    :param optionals: List of products which we will ignore them, mean will not buy it
    :param ingredients: For each product in ingredients the argument is the name of the product
                        and the value is the amount tha necessary (in gram)
    :return: The total price
    """
    total = 0
    for p in prices:
        if p in optionals:
            continue
        total = total + prices[p] * ingredients[p] // 100

    return total
