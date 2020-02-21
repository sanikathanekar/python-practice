bill=0
print("Menu")
print("1. Pen\t\t10\n2. Pencil\t5\n3. Eraser\t5")
c=input("Select an item-")
if c==1:
    print("Pen")
    q=input("Enter Quantity-")
    bill=bill+(10*q)
print(bill)
