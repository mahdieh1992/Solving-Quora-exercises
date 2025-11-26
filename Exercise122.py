# Abstract method
from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def call_Suv(self):
        pass 
    
    @abstractmethod
    def call_Coupe(self):
        pass 
    
class BMW(Car):
    def call_Suv(self):
        return X1()
    
    def call_Coupe(self):
        return M2()
    
class Benz(Car):
    def call_Suv(self):
        return Gla()
    
    def call_Coupe(self):
        return Cls()
    
class Suv(ABC):
    @abstractmethod
    def create_suv(self):
        pass

class Coupe(ABC):
    @abstractmethod
    def create_coupe(self):
        pass

class X1(Suv):
    def create_suv(self):
        return f"this is x1 ...."
    
class M2(Coupe):
    def create_coupe(self):
        return f"this is M2 ...."
    
    
class Gla(Suv):
    def create_suv(self):
        print("this is Gla ....")
    
class Cls(Coupe):
    def create_coupe(self):
        return f"this is Cls ...."
    
    
def client_suv(order):
    brands = {
        'bmw':BMW,
        'benz':Benz
    }
    suv = brands[order]().call_Suv()
    suv = suv.create_suv()
    
    
    
print(client_suv('benz'))