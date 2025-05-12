from abc import ABC, abstractmethod

#create Product Interface

class FootWear(ABC):
    @abstractmethod
    def get_footwear(self):
        pass
    
#create concrete classes

class Loafer(FootWear):
    def get_footwear(self):
        return "Here is your Loafer !"
    
class Sneakers(FootWear):
    def get_footwear(self):
        return "Here is your Sneakers !"
    
class Boot(FootWear):
    def get_footwear(self):
        return "Here is your Boot !"
    
class FlipFlops(FootWear):
    def get_footwear(self):
        return "Here is your FlipFlops !"

class Sandals(FootWear):
    def get_footwear(self):
        return "Here is your Sandals !"
    
#create a footwear-machine
class FootWearMachine:
    def get_item(self,footwear):
        if footwear == "Loafer":
            return Loafer().get_footwear()
        elif footwear=="Sneakers":
            return Sneakers().get_footwear()
        elif footwear=="Boot":
            return Boot().get_footwear()
        elif footwear == "FlipFlops":
            return FlipFlops().get_footwear()
        elif footwear == "Sandals":
            return Sandals().get_footwear()
        
        else:
            return "Unknown Footwear"
        
        
if __name__ == "__main__":
    footwear = FootWearMachine()
    
    item = footwear.get_item('Loafer')
    print(item)
    item=footwear.get_item('Sneakers')
    print(item)
    item=footwear.get_item('Boot')
    print(item)
    item=footwear.get_item('FlipFlops')
    print(item)
    item=footwear.get_item('Sandals')
    print(item)
    
    

        
