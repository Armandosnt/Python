class House:
    
    def __init__(self,capacity):
        self.capacity = capacity
        
    def __add__(self, other):
        return House(self.capacity + other.capacity)  
        
    def __nul__(self, other):
        return "House can not be multiplied by anoother house"
        
A = House(10)
B = House(15)    
C = A + B
print(A * B )