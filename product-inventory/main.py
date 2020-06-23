import calculation

def help():
    print("\n****************************************\nFormat for adding items: 'a,Item Name, Item Number, Item price'\n****************************************")
    print("****************************************\nFormat for seling items: 's,Item Name, Item Number'\n****************************************\n")


#Display total number and total value of inventory
def current_stock(inventory):
    if inventory:
        for oneDict in inventory:
            for k, v in oneDict.items():
                print("{} : {}" .format(k, v))
            print("*" * 10)
            sumOfStock, sumOfValue = calculation.get_current_stock(inventory)

        print("*** Total stock is: {}. ***" .format(sumOfStock))
        print("*** Total stock value: {}$. ***".format(sumOfValue))

    else:
        print("Inventory is empty!")

def try_again():
    print("Please try again. I don't understand.")

def main():
    inventory = (calculation.load_from_file())

    while True:
        userInput = input("Choices:\n[H] for [H]elp on information how to Add or Sell items.\n[A] and amount to [A]dd.\n[S] and amount to [S]ell\n[L] to [L]ist current stock\n[x] for E[x]it.\nEnter command: ")
        userInput  = userInput.upper().split(',')

            #On exit show current stock and break
        if userInput[0] == "X":
            current_stock(inventory)
            print("Good bye !")
            break

        elif userInput[0] =="H":
            help()

        #Show current stock
        elif userInput[0] == "L":
            current_stock(inventory)

        #On Add stock call add function from calculation module
        elif userInput[0] == "A":
            inventory = calculation.add(userInput, inventory)

        # On Sell stock call sell function from calculation module
        elif userInput[0] == "S":
            inventory = calculation.sell(userInput, inventory)
        else:
            try_again()

    #Save current inventory situation for later use
    calculation.save_to_file(inventory)

if __name__=="__main__":
    main()