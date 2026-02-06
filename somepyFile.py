n=int(input("Enter a number: "))
class Home:
    def __init__(self,name,age,numbers):
        self.name=name
        self.age=age
        self.numbers=numbers
    def greet(self):
        print("hello",self.name)
shirou=Home("shirou",20,536835787)
rin=Home("rin",18,536835788)
shirou.greet()
rin.greet()
print("Number of shirou:",shirou.numbers)