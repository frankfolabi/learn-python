requested_toppings = ['mushrooms', 'green peppers', 'extra cheese' ]

if requested_toppings != 'anchovies':
    print("Hold the anchovies")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':   
        print("Sorry, green peppers don finish.")    
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


#######################################
# Building from empty list
requested_toppings = []

if requested_toppings:   
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print(f"You sure say na plain pizza you want?")

available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'olives', 'pineapples', 'pepperoni']


requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Abeg we no get that {requested_topping} again")
print("\nYour pizza don ready")



