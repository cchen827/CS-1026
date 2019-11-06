#MENU COSTS
egg = float(0.99)
bacon = float(0.49)
sausage = float(1.49)
hash_brown = float(1.19)
toast = float(0.79)
coffee = float(1.09)
tea = float(0.89)

# INITIALIZING OTHER RELEVANT VARIABLES TO BE USED IN THE LOOP
customer_order = 0
quantity = 0
preTaxTotal = 0

tax = float(0.13)

# ERROR TRAPPING FOR INPUT
def formatInput(textLine) :
 textLine = textLine.lower().strip()
 wordList = textLine.split()
 textLine = " ".join(wordList)
 return textLine


print("Welcome to Good Morning America!")

print("")


while customer_order != "q": # WHILE LOOP TO REPEAT INSTRUCTIONS
    customer_order = input("Enter (item q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
    customer_order = formatInput(customer_order) # REFER BACK TO DEFINITION

    if customer_order == "egg":
        customer_order = float(egg)

    elif customer_order == "bacon":
        customer_order = float(bacon)

    elif customer_order == "sausage":
        customer_order = float(sausage)

    elif customer_order == "hash brown":
        customer_order = float(hash_brown)

    elif customer_order == "toast":
        customer_order = float(toast)

    elif customer_order == "coffee":
        customer_order = float(coffee)

    elif customer_order == "tea":
        customer_order = float(tea)

    elif customer_order == "small breakfast":
        customer_order = float(egg + hash_brown + 2*toast + 2*bacon + sausage)

    elif customer_order == "regular breakfast":
        customer_order = float(2*egg + hash_brown + 2*toast + 4*bacon + 2*sausage)

    elif customer_order == "big breakfast":
        customer_order = float(3*egg + 2*hash_brown + 4*toast + 6*bacon + 3*sausage)

    elif customer_order == "q":
        break

# SECOND SET OF INSTRUCTIONS
    quantity = str(input("Please enter a quantity: "))  # THIS IS OUTSIDE THE WHILE LOOP

# ERROR TRAPPING
    if quantity.isnumeric():
        quantity = int(quantity)
        preTaxTotal += customer_order * quantity

    else:
        print("The quantity you have inputted is invalid. Please try again")
        continue


Cost_tax = preTaxTotal*tax

print("Pre-tax total: $ %.2f" % preTaxTotal)
print("Tax: $ %.2f" % Cost_tax)
print("Total: $ %.2f" %(Cost_tax + preTaxTotal))
