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
count_B = 0
count_C = 0
count_D = 0
for product in selected_products:
    if product == "A":
        count_A += 1
    elif product == "B":
        count_B += 1
    elif product == "C":
        count_C += 1
    elif product == "D":
        count_D += 1


total_price = 0
while count_A > 0:
    if count_A >= 3:
        total_price += 130
        count_A -= 3
    else:
        total_price += count_A * products["A"]
        count_A = 0
while count_B > 0:
    if count_B >= 2:
        total_price += 45
        count_B -= 2
    else:
        total_price += count_B * products["B"]
        count_B = 0
total_price += (count_C * products["C"]) + (count_D * products["D"])

print(total_price)  
