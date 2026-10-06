kettle_boiled = True

if kettle_boiled:
    print(f"Kettle done, time to sever hot water") 

# if and else
snack = input("Please enter your order: ").lower()
print(f"user orderd: {snack}")
if snack == "samosa" or snack == "cookie":
    print("your order will be ready in 5 mins")
else:
    print("we are sorry, we server currently only cookies, samosa and tea")

# if , elif and else
cup_size = input("please choose cup size: (small/medium/large): ").lower()
if cup_size == "small":
    print("The price of small cup is 10Rs")
elif cup_size == "medium":
    print("The price of medium cup is 15Rs")
elif cup_size == "large":
    print("The price of large cup is 20Rs")
else:
    print("Unkown cup size")

# if and else chaining inside a if condition(nesting if else)
device_active = "Active"
temp = 40

if device_active == "Active":
    if temp >35:
        print("High Temperature")
    else:
        print("normal Temperature")
else:
    print("Device is off, Please Turn on")

# Ternary Operator

order_amount = int(input("Your order amount is: "))
print(f"your order amount is {order_amount}")
delivery_fees = 0 if order_amount > 300 else 30
print(f"Your delivery fees is {delivery_fees}")

# match case conditioning

seat_type = input("select the seat type (Sleeper, 3AC, 2AC, 1AC): ").lower()

match seat_type:
    case "sleeper":
        print("40 seats available")
    case "3ac":
        print("60 seats available")
    case "2ac":
        print("30 seats available")
    case "1ac":
        print("20 seats available")
    case _:
        print("General no need for reservation")

# walrus (:=)

chais = ["lemon","ginger", "cinnomon", "chocolate"]

value = 13

if reminder := value % 5:
    print(f"not divisble the remider is {reminder}") 
