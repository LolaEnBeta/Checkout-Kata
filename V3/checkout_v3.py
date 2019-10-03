from Cart import Cart

# A = 50 --- 3x130
# B = 30 --- 2x45
# C = 20
# D = 15

prices = {"A": 50, "B": 30, "C": 20, "D": 15}

cart = Cart()

finish = False

while finish != True:
    item = input("Select an item or writte exit to finish: ")

    if item in prices:
        cart.add_item(item)
