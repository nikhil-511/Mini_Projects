#This is OOPS program in python which is used to display the OOPS concepts in python.
#Class declaration, Object declaration, __init__, instance variable, static variable,
#instance method, static method, class method, decorators, Inheritance.
#Class declaration  -> It is a blue print.
#Object declaration -> It is an instance of a class.
#__init__           -> It is a constructor method to declare instance variables.
#instance variable  -> Variables that belong to an object and can only be called using object or class.
#static variable    -> Variables that belong to no one and can only be called using class.
#instance method    -> Method that belong to an object and can only be called using object or class.
#static method      -> Method that belong to no one and can only be called using class.
#class method       -> Method that belong to a class and can only be called using class.
#decorators         -> 
#Inheritance        -> Ability to get features of other classes.

class computer:
    device="Computer"                       #device is a static variable
    def __init__(self):                     #__init_ is like a constructor which excepts the object self
        self.processor = "Intel i5 11th gen"
        self.RAM = 16
        self.SSD = 512
        self.graphics_card = "None"         #self.--- are instance variables
        
    def ShowConfig(self):
        print("Device:",computer.device)    #computer.device is the way to call an static variable
        print("Configuration of the computer:")
        print("Processor:",self.processor)  #self.processor is the way to call an instance variable
        print("RAM:",self.RAM)
        print("SSD:",self.SSD)
        print("Graphics Card:",self.graphics_card)
        print("\n")
        
    def UpdtConfig(self,pro,ram,ssd,gc):
        self.processor = pro
        self.RAM = ram
        self.SSD = ssd
        self.graphics_card = gc

    @staticmethod
    def GetConfig():
        print("Device:",computer.device)    #computer.device is the way to call an static variable
        print("Configuration of the computer:")
        print("Processor:",computer.processor)  #self.processor is the way to call an instance variable
        print("RAM:",computer.RAM)
        print("SSD:",computer.SSD)
        print("Graphics Card:",computer.graphics_card)
        print("\n")
        
class student(computer):
    def __init__(self):
        self.st_id=511
        self.st_name="NEO"
        self.st_branch="CSE"
        self.st_prof="Student"
        
    def ShowInfo(self):
        print("Information avaliable are..")
        print("ID no:",self.st_id)
        print("Name:",self.st_name)
        print("Branch:",self.st_branch)
        print("Profession:",self.st_prof)
        print("\n")

    def UpdtInfo(self,d,name,branch,prof):
        st_id=d
        st_name=name
        st_branch=branch
        st_prof=prof
        
user1=computer()                        #object declaration user1 is an object
user2=computer()                        #object declaration user2 is an object
user1.UpdtConfig("Ryzen",16,512,"YES")  #the way to change values using method
user1.ShowConfig()                      #user1.ShowConfig() is the way to call an instance method 
user2.ShowConfig()

sdnt1=student()
sdnt2=student()
sdnt2.UpdtInfo(511,"Nikhil","CSE","Student")
sdnt1.ShowInfo()
print("Required laptop configuration is")
sdnt1.GetConfig()
sdnt2.ShowInfo()
print("Required laptop configuration is")
sdnt2.UpdtConfig("Intel i3",16,512,"NO")
sdnt2.ShowConfig()






