from abc import ABC, abstractmethod

#create Product Interface

class FootWear(ABC):
    @abstractmethod
    def get_footwear(self):
        pass
    
#create concrete classes

class Loafer(FootWear):
    def get_footwear(self):
        return "Here is your Loafer!"
    
class Sneakers(FootWear):
    def get_footwear(self):
        return "Here is your Sneakers"
    
class Boot(FootWear):
    def get_footwear(self):
        return "Here is your Sneakers"
    
class FlipFlops(FootWear):
    def get_footwear(self):
        return "Here is your Sneakers"

class Sandals(FootWear):
    def get_footwear(self):
        return "Here is your Sandals"
    
#create a footwear-machine
class FootWearMachine:
    def get_item(self,footwear):
        if isinstance(footwear, Loafer) or isinstance(footwear,Sneakers) or isinstance(footwear,Boot) \
            or isinstance(footwear,FlipFlops) or isinstance(footwear,Sandals):
            return footwear.get_footwear()
        
        else:
            return "Unknown Footwear"
        
        
if __name__ == "__main__":
    footwear = FootWearMachine()
    
    item = footwear.get_item(Loafer())
    print(item)
    item=footwear.get_item(Sneakers())
    print(item)
    item=footwear.get_item(Boot())
    print(item)
    item=footwear.get_item(FlipFlops())
    print(item)
    item=footwear.get_item(Sandals())
    print(item)
    
    

        
