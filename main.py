from menu import menu , resources



money = 0
def check_resources(order):
    if (resources["water"]>=menu[order]["ingredients"]["water"]) and (resources["milk"]>=menu[order]["ingredients"]["milk"]) and (resources["coffee"]>=menu[order]["ingredients"]["coffee"]):
        return True
    else:
        return False


def process_coins(order):           # machine takes only coins
    quarters = float(input("how many quarters ? "))
    dimes = float(input("how many dimes ? "))
    nickels = float(input("how many nickels ? "))
    pennies = float(input("how many pennies ? "))
    money_paid = ((quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01))
    amt = menu[order]["cost"]
    if money_paid >= amt:       # user money and actual cost is checked
        global money
        money = amt
        resources["water"]-=menu[order]["ingredients"]["water"]
        resources["milk"] -= menu[order]["ingredients"]["milk"]
        resources["coffee"] -= menu[order]["ingredients"]["coffee"]
        print(f"Enjoy your {order} ")
        if money_paid > amt:
            print(f"Your change is {round(money_paid-amt , 2)}")
    else:
        print("Sorry that's  not enough money. Money refunded.")

def report(order):
    if order=="report":     # to check resources present in machine
        for key,value in resources.items():
            print(f"{key} : {value}")
        print(f"Money :  $ {round(money,2)} ")
    else:
        if check_resources(order):
            process_coins(order)
        else:
            print("Not enough resources to process the order.")


off = False
while not off:      # machine will turn off when "off" becomes true
    ord = input("What would you like? (espresso/latte/cappuccino):")
    report(ord)     # function call
    operator = input("Are you a machine operator ?(y/n) ")   # if you are a machine operator the machine will turn off
    if operator=="y":                                        # otherwise the loop continues
        off = True
