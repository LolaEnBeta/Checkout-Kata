from Cart import Cart

# A = 50 --- 3x130
# B = 30 --- 2x45
# C = 20
# D = 15

prices = {"A": 50, "B": 30, "C": 20, "D": 15}
offers = {
    "A": {
        "units": 3,
        "price": 130
    },
    "B": {
        "units": 2,
        "price": 45
    }
}

def start_buying():
    finish = False
    while finish != True:
        print("")
        print(prices)
        item = input("Select an item or writte exit to finish: ")

        if item in prices:
            cart.add(item)
        elif item == "exit":
            finish_buying()
            finish = True
        else:
            print("We don't have this item. Please, try again =)")

def finish_buying():
    print("Total to pay: ", cart.calculate_total_price(offers, prices))

cart = Cart()
start_buying()
