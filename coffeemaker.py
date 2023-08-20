from drink import Drink
class CoffeeMachine:
    def __init__(self, water, milk, coffee,money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money  

    def report(self):
        print(f'Water: {self.water}')
        print(f'Milk: {self.milk}')
        print(f'Coffee: {self.coffee}')
        print(f'Money: {self.money}')

    def check_ressources(self,drink):
        if drink.water <= self.water:
            if drink.milk <= self.milk:
                if drink.coffee <= self.coffee:
                    return True
                else:
                    print('Not enough coffee in machine!')
            else:
                print('Not enough milk in machine!')        
        else:
            print('Not enough water in machine!')

    def process_coins(self):
        money = 0
        while True:
            coins = input('Insert coins: ')
            if coins == 'quarter':
                money+= 0.25
                print(f'Your balance: {money}$')
            elif coins == 'dime':
                money+= 0.10
                print(f'Your balance: {money}$')
            elif coins == 'nickle':
                money+= 0.05
                print(f'Your balance: {money}$')
            elif coins == 'pennies':
                money+=0.01
                print(f'Your balance: {money}$')
            elif coins == 'done':
                print(f'Your balance: {money}$')
                break
            else:
                print('Please insert coins.')    
        return money
                    

    def check_transaction(self, drink):
        money = CoffeeMachine.process_coins(self)
        if money< drink.price:
            print("Sorry that's not enough money. Money refunded.")
        elif money>= drink.price: 
            self.money += drink.price
            self.milk -= drink.milk
            self.coffee -= drink.coffee
            self.water -= drink.water
            print(f'Here is your {drink.name}. Enjoy!')
            if money> drink.price:
                change = money-drink.price
                print(f'Here is {change}$ in change.')

    def order(self):
        choice = input("What would you like? (espresso/latte/cappuccino/report/nothing): ")  
        if choice == "espresso":
            drink = Drink('espresso',2.5,100,90,12)
            CoffeeMachine.check_ressources(self,drink)
            if CoffeeMachine.check_ressources(self,drink) == True:
                CoffeeMachine.check_transaction(self,drink)
        elif choice == "latte":
            drink = Drink('latte',3,120,90,15)
            CoffeeMachine.check_ressources(self,drink)
            if CoffeeMachine.check_ressources(self,drink) == True:
                CoffeeMachine.check_transaction(self,drink)
        elif choice == "cappuccino":
            drink = Drink('cappuccino',2.5,90,80,20)
            CoffeeMachine.check_ressources(self,drink)
            if CoffeeMachine.check_ressources(self,drink) == True:
                CoffeeMachine.check_transaction(self,drink)
        elif choice == "report":
            CoffeeMachine.report(self)
        elif choice == 'nothing':
            print('Have a great day!')
            quit()    
        elif choice == "off":
            print('Machine off!')
            quit()
        else:
            print('Invalid choice!')