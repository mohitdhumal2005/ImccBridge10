class Rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        return self.l * self.b
    
    def perimeter(self):
        return 2*(self.l+self.b)

ob1=Rect(50,20)
print(ob1.area())
print(ob1.perimeter())