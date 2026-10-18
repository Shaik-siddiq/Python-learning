# for loop with range
for token in range(1,11):
    print(f"serving Chai token no #{token}")

orders = ["sid", "zeba", "aisha", "shaik", "khasim", "akthar"]

for name in orders:
    print(f"order is reday for {name}")

menu = ["Black Tea", "Black Coffee", "Lemon Tea", "Tea", "Coffee", "Irani Chai", "Cinnomon Tea"]

# for loop with enumerate
for indx, m in enumerate(menu, start=1):
    print(f"{indx} : {m}")

amount = [30, 10, 10, 40, 100, 20]

# for loop with zip
for name, paid in zip(orders, amount):
    print(f"{name} paid {paid} rupees")

temp = 40

# while loop
while temp <100:
    print(f"current temp {temp}")
    temp += 15
print(f"Tea is ready to serve")

flavours = ["ginger", "lemon", "out of stock", "cinnomon", "discountinued", "tulasi" ]

# continue and break
for flavour in flavours:
    if flavour == "out of stock":
        print(f"we are sorry for {flavour}")
        continue
    if flavour == "discountinued":
        print(f"Please try after some the some time the server is {flavour}")
        break
    print(f"the flavour is {flavour}")

staff_tuples = [("sid", 34), ("zeba", 28), ("aisha", 33), ("khasim", 39), ("akthar", 51)]

# for and else loop
for name, tasks in staff_tuples:
    if tasks >=35:
        print(f"{name} is got promoted as senior")
        break
else:
        print("No one promoted this year")

# while with walrus

while (fla := input("choose your flavour: ")) not in menu:
    print(f"we are sorry {fla} is not in the flavours, please choose these {menu}")
   
print(f"your order is {fla}")

# {"Key":"value"} is called as dictionaries
users = [
    {"id":1, "total":100, "coupon":"P10"},
    {"id":2, "total":300, "coupon":"G90"},
    {"id":3, "total":120, "coupon":"N10"}
]

discounts = {
    "P10":(0.2,0),
     "G90":(0.5,0),
     "N10":(0, 20)
}

for user in users:
    percent, flat_disc = discounts.get(user["coupon"], (0,0))
    after_discount = user["total"] - (percent * 100) - flat_disc
    print(f"for {user["id"]} the total is {user['total']} and after discounted price is {after_discount}")