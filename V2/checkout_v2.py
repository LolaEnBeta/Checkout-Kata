""" A=50        3 for 130
    B=30        2 for 45
    c=20
    D=15
"""

products = {"A": 50, "B": 30, "C": 20, "D": 15}
print(products)

selected_products = []
selected_product = input ("Select one item from de list: ")

while selected_product != "":
    selected_products.append(selected_product)
    print(selected_products)
    selected_product = input ("Select one item from de list: ")

checkout = []

for product in selected_products:
    prices = products[product]
    checkout.append(prices)

print(selected_products)
print("Total to pay: ", sum(checkout))
