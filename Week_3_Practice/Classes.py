class MyClass:
    
    def __init__(self):
        self.data = []

    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
x.data.append("Brian")

print(x.data)
print(x.i)

printMe = x.f()

print(x.f)
print(printMe)

y = MyClass()

# Write Python3 code here 
  
class MyCar(): 
      
    # init method or constructor 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 
          
    def show(self): 
        print("Model is", self.model ) 
        print("color is", self.color ) 
          
# both objects have different self which  
# contain their attributes 
audi = MyCar("audi a4", "blue") 
ferrari = MyCar("ferrari 488", "green") 
bmw = MyCar("BMW M4","black")
  
audi.show()     # same output as car.show(audi) 
ferrari.show()  # same output as car.show(ferrari) 
bmw.show() 

  
# Behind the scene, in every instance method  
# call, python sends the instances also with 
# that method call like car.show(audi) 


