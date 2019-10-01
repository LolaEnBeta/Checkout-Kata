# A = 50 --- 3x130
# B = 30 --- 2x45
# C = 20
# D = 15

items = [50, 30]

def sum_checkout(items):
    total_price = 0
    for item in items:
        total_price += item
    return total_price

def sum_checkout_items_from_dictionary(items):
    total_price = items["A"] + items["B"]
    return total_price
