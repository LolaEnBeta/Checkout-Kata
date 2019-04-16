items = {"A": 50, "B": 30, "C": 20, "D": 15}
checkout = list()

print(items)

n = 1
while n > 0:
    select_item = input("Choose one item from the list (for exit press Enter): ")
    checkout.append(select_item)
    if select_item == "":
        checkout.remove(select_item)
        n = 0
        break
    if select_item not in items:
        print("We don't have this yet, sorry!")
        checkout.remove(select_item)
    

        
print("You choose this these items:", checkout)
