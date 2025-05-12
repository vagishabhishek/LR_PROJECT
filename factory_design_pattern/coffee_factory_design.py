from abc import abstractmethod,ABC

#Step 1: Define the Product Interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass
    
#Step 2: Implement Concrete Products
class Espresso(Coffee):
    def prepare (self):
        return 'Preparing a rich and strong Espresso !'
    
class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte !"
    
class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy Cappuccino !"
    
#Step 3 :Create the factory(CoffeeMachine)
class CoffeeMachine:
    
    def make_coffee(self,coffee_type):
        if coffee_type == 'Espresso':
            return Espresso().prepare()
        
        if coffee_type == 'Latte':
            return Latte().prepare()
        
        if coffee_type == 'Cappuccino':
            return Cappuccino().prepare()
        
        else:
            return "Unkwn Coffee Type"
        
#step 4: Use the factory to create Products
if __name__ == "__main__":
    machine = CoffeeMachine()
    coffee = machine.make_coffee('Espresso')
    print(coffee) 
    
    coffee = machine.make_coffee('Latte')
    print(coffee)
    
    coffee = machine.make_coffee('Cappuccino')
    print(coffee)