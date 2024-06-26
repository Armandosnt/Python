class House:
    
    def __init__(self,capacity):
        self.capacity = capacity
        
    def __add__(self, other):
        return House(self.capacity + other.capacity)  
       
A = House(10)
B = House(15)    
C = A + B
print(C.capacity)