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

count_A = 0
for product in selected_products:
    if product == "A":
        count_A += 1

total_price = 0
while count_A > 0:
    if count_A >= 3:
        total_price += 130
        count_A -= 3
    else:
        total_price += count_A * 50
        count_A = 0

print(total_price)  
