
class CashRegister:
    def __init__(self, cashOnHand: int = 500):
        if cashOnHand < 0:
            self.cashOnHand = 500
        else:
            self.cashOnHand = cashOnHand
    def currentBalance(self):
        return self.cashOnHand

    def acceptAmount(self, AmountIn: int):
        self.cashOnHand = self.cashOnHand+AmountIn
class Dispenser:
    def __init__(self, cost: int = 50, numberOfItems: int = 50):
        if cost and numberOfItems < 0:
            self.cost = 50
            self.numberOfItems = 50
        else:
            self.cost = cost
            self.numberOfItems = numberOfItems
    def getCount(self):
        return self.numberOfItems
    def getProductCost(self):
        return self.cost
    def makeSale(self):
        self.numberOfItems -= 1
def showSelection():
    print("""
***** Welcome to Sweet's Candy Shop *****
Select something in the following options
0  View Balance                             
1  Candy       ~     5 cents  
2  Chips       ~    15 cents
3  Gum         ~     5 cents
4  Cookies     ~    20 cents
5  Exit
    """)
def sellProduct(cRegister : CashRegister, product : Dispenser):
    try:
        if product.getCount() > 0:
           print(product.getCount(), "piece(s) available", " and costs", product.getProductCost(), " cents each.")
           print()
           amountIn= int(input(f"Kindly enter {product.getProductCost()} cents for a piece of it: "))
           if 0 < amountIn == product.getProductCost():
              cRegister.acceptAmount(amountIn)
              product.makeSale()
              print("Thank you for the purchase!")
              return
           elif 0 < amountIn < product.getProductCost():
               while amountIn != product.getProductCost() and amountIn != "":
                   mAmount = product.getProductCost() - amountIn
                   nAmount = int(input(f"The amount you entered is insufficient, kindly enter the missing {mAmount} cents:"))
                   if mAmount == nAmount:
                       amountIn = amountIn+nAmount
                       cRegister.acceptAmount(amountIn)
                       product.makeSale()
                       print("Thank you for the purchase!")
                       break
                   elif nAmount > mAmount:
                       x = nAmount-mAmount
                       y = nAmount-x
                       amountIn = amountIn+y
                       cRegister.acceptAmount(amountIn)
                       print(f"your change is {x}.")
                       product.makeSale()
                       print("Thank you for the purchase!")
                       break
                   else:
                       continue
           elif amountIn > product.getProductCost():
               x = amountIn - product.getProductCost()
               y = amountIn - x
               cRegister.acceptAmount(y)
               product.makeSale()
               print(f"Your change is {x} cent(s).")
               print("Thank you for the purchase!")
           else:
               print("The payment should be greater than 0")
        else:
            print("Sorry, the item is already sold out.")
    except ValueError:
        print("You inputted nothing or invalid input.")
def Main_Program():
    candy = Dispenser(5, 2)
    chips = Dispenser(15, 3)
    gum = Dispenser(5, 10)
    cookies = Dispenser(20, 7)
    Candy_Machine = CashRegister(100)
    while True:
        showSelection()
        try:
            choice = int(input("Enter your choice: "))
            print()
            match choice:
                case 0:
                    print("The current register balance is", CashRegister.currentBalance(Candy_Machine), "cents.")
                    print("Candies left: ",candy.getCount()," pieces")
                    print("Chips left :  ",chips.getCount()," pieces")
                    print("Gums left:    ",gum.getCount()," pieces")
                    print("Cookies left: ",cookies.getCount()," pieces")
                case 1:
                    print("You chose candies.")
                    sellProduct(Candy_Machine, candy)
                case 2:
                    print("You chose chips.")
                    sellProduct(Candy_Machine, chips)
                case 3:
                    print("You chose gums.")
                    sellProduct(Candy_Machine, gum)
                case 4:
                    print("You chose cookies.")
                    sellProduct(Candy_Machine, cookies)
                case 5:
                    print("Program Exit.")
                    break
                case _:
                    print("Your input is not within the choices.")
                    continue
        except ValueError:
            print("Invalid Input")
            print()
Main_Program()
