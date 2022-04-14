class A:
    def display(self):
        print("In display of class A")        


class B(A):
    def display(self):
        print("In display of class B")        

a1=B()
a1.display()
