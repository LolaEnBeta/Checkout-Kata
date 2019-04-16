items = {"A": 50, "B": 30, "C": 20, "D": 15}
checkout = list()

print(items)

n = 1
while n > 0:
    select_item = input("Choose one item from the list (for exit press Enter): ")
    if select_item == "":
        n = 0
    checkout.append(select_item)
    if "" in checkout:
        checkout.remove("")
print(checkout)
