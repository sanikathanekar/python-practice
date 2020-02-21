bill=float()
while True:
    print("1 - veg\n2 - Non-veg\n3 - for Exit")
    c=int(input("Select->"))
    if c==1:
        while True:
            print("*"*30)
            print("Veg Menu")
            print("1 - Starter\n2 - Main Course\n3 - Exit")
            c=int(input("Select->"))
            if c==1:
                while True:
                    print("*"*30)
                    Print("Starter Menu")
                    print("1-Cheese Balls ~Rs.250\n2-Harabhara Kabab~Rs.200\n3-Paneer Tikka~Rs.280\n4-Exit")
                    c=int(input("Select->"))
                    if c==1:
                        print("Cheese Balls")
                        q=int(input("Quantity-"))
                        bill=bill+(250*q)
                    elif c==2:
                        print("Harabhara Kabab")
                        q=int(input("Quantity-"))
                        bill=bill+(200*q)
                    elif c==3:
                        print("Paneer Tikka")
                        q=int(input("Quantity-"))
                        bill=bill+(280*q)
                    elif c==4:
                        break
                    else:
                        print("Select an Item from the Menu")
            elif c==2:
                while True:
                    print("*"*30)
                    print("Main Course")
                    print("1-Veg Handi ~Rs.250\n2-Paneer Makhanwala~Rs.200\n3-Paneer Tikka Masala~Rs.280\n4-Exit")
                    c=int(input("Select->"))
                    if c==1:
                        print("Veg Handi")
                        q=int(input("Quantity-"))
                        bill=bill+(250*q)
                    elif c==2:
                        print("Paneer Makhanwala")
                        q=int(input("Quantity-"))
                        bill=bill+(200*q)
                    elif c==3:
                        print("Paneer Tikka Masala")
                        q=int(input("Quantity-"))
                        bill=bill+(280*q)
                    elif c==4:
                        break
                    else:
                        print("Select an Item from the Menu")
            elif c==3:
                break
            else:
                ("Select option from the menu")

    elif c==2:
        while True:
            print("*"*30)
            print("Non-Veg Menu")
            print("1 - Starter\n2 - Main Course\n3 - Exit")
            c=int(input("Select->"))
            if c==1:
                while True:
                    print("*"*30)
                    print("Starter Menu")
                    print("1-Chicken lolypop ~Rs.250\n2-Seekh Kabab~Rs.250\n3-Chicken Tikka~Rs.280\n4-Exit")
                    c=int(input("Select->"))
                    if c==1:
                        print("Chicken lolypop")
                        q=int(input("Quantity-"))
                        bill=bill+(250*q)
                    elif c==2:
                        print("Seekh Kabab")
                        q=int(input("Quantity-"))
                        bill=bill+(250*q)
                    elif c==3:
                        print("Chicken Tikka")
                        q=int(input("Quantity-"))
                        bill=bill+(280*q)
                    elif c==4:
                        break
                    else:
                        print("Select an Item from the Menu")
            elif c==2:
                while True:
                    print("*"*30)
                    print("Main Course")
                    print("1-Chicken Handi ~Rs.250\n2-Chicken Makhanwala~Rs.250\n3-Chicken Tikka Masala~Rs.280\n4-Exit")
                    c=int(input("Select->"))
                    if c==1:
                        print("Chicken Handi")
                        q=int(input("Quantity-"))
                        bill=bill+(250*q)
                    elif c==2:
                        print("Chicken Makhanwala")
                        q=int(input("Quantity-"))
                        bill=bill+(250*q)
                    elif c==3:
                        print("Chicken Tikka Masala")
                        q=int(input("Quantity-"))
                        bill=bill+(280*q)
                    elif c==4:
                        break
                    else:
                        print("Select an Item from the Menu")
            elif c==3:
                break
            else:
                ("Select option from the menu")
    elif c==3:
        break
    else:
        print("Select a valid choice")
print("*"*30)
Print("Bill")
sgst=(9/100)*bill
print("9% SGST-",sgst)
cgst=(8/10)*bill
print("8% CGST-",cgst)
bill=bill+sgst+cgst
print("Total Bill", bill)
    
    
        
